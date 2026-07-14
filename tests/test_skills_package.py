"""Tests for the skills/ package: every skill bundle, the manifest, the
index, and both installer scripts.

These guards keep every skill honest about what it claims to summarize: a
skill can never silently drift from the guide it packages, because its
declared `source` paths are checked against the real file tree on every
run, and it can never go missing from the installer's manifest without the
test suite noticing.
"""
import importlib.util
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def load_script(name):
    script = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


discover_ai_sources = load_script("discover_ai_sources")
install_skill = load_script("install_skill")
mechanical_research_expansion = load_script("mechanical_research_expansion")

REQUIRED_SECTIONS = (
    "## Trigger",
    "## Purpose",
    "## Inputs",
    "## Scope",
    "## Procedure",
    "## Verification",
    "## Failure Cases",
    "## Final Report",
    "## Disable Path",
)

REQUIRED_FRONTMATTER_KEYS = ("name", "description", "category", "source")

ALLOWED_CATEGORIES = {
    "tools",
    "prompts",
    "codex-workflow",
    "hermes",
    "image-generation",
    "guides",
    "meta",
}

REQUIRED_SKILL_SLUGS = {
    "use-codex-safely",
    "self-directed-goal-runner",
    "create-a-new-skill",
    "install-this-skill-pack",
}


def parse_frontmatter(text):
    """Minimal parser for this repo's controlled skill frontmatter shape.

    Handles `key: value` scalars and `key:` followed by `- item` list
    entries. Deliberately not a general YAML parser -- the frontmatter
    shape here is small and fixed by skills/README.md.
    """
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    block = text[4:end]
    body = text[end + 5 :]

    data = {}
    current_list_key = None
    for raw_line in block.split("\n"):
        if not raw_line.strip():
            continue
        if raw_line.startswith("  - ") or raw_line.startswith("- "):
            item = raw_line.strip()[2:].strip().strip('"')
            if current_list_key:
                data.setdefault(current_list_key, []).append(item)
            continue
        if ":" in raw_line:
            key, _, value = raw_line.partition(":")
            key = key.strip()
            value = value.strip()
            if value:
                data[key] = value.strip('"')
                current_list_key = None
            else:
                data[key] = []
                current_list_key = key
    return data, body


def iter_skill_dirs():
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())


def load_manifest():
    manifest_path = SKILLS_DIR / "manifest.json"
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def duplicate_values(values):
    return sorted(value for value, count in Counter(values).items() if count > 1)


def ordered_sequences_match(expected, actual):
    return list(expected) == list(actual)


def git_tree_entries(root):
    result = subprocess.run(
        ["git", "-C", str(root), "ls-tree", "-rz", "--full-tree", "HEAD"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    entries = {}
    for record in result.stdout.split(b"\0"):
        if not record:
            continue
        metadata, path_bytes = record.split(b"\t", 1)
        mode, object_type, object_id = metadata.decode("ascii").split()
        path = path_bytes.decode("utf-8", "surrogateescape")
        if path in entries:
            raise AssertionError(f"duplicate Git tree path: {path}")
        entries[path] = {
            "mode": mode,
            "type": object_type,
            "oid": object_id,
        }
    return entries


def committed_source_blob(root, source, entries):
    resolved = resolve_declared_source(root, source)
    relative = Path(source).as_posix()
    entry = entries.get(relative)
    if entry is None:
        raise ValueError(f"source path is not committed at HEAD: {source}")
    if entry["mode"] not in {"100644", "100755"} or entry["type"] != "blob":
        raise ValueError(f"source path must be a regular Git blob: {source}")
    if not resolved.is_file():
        raise ValueError(f"source path must resolve to an existing repository file: {source}")
    if "blob" in entry:
        return entry["blob"]
    blob = subprocess.run(
        ["git", "-C", str(root), "cat-file", "blob", entry["oid"]],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout
    object_bytes = b"blob " + str(len(blob)).encode("ascii") + b"\0" + blob
    object_hash = hashlib.sha256 if len(entry["oid"]) == 64 else hashlib.sha1
    computed_oid = object_hash(object_bytes).hexdigest()
    if computed_oid != entry["oid"]:
        raise AssertionError(f"Git blob identity mismatch for {source}")
    entry["blob"] = blob
    entry["sha256"] = hashlib.sha256(blob).hexdigest()
    return blob


def parse_index_slugs(index_text):
    row_pattern = re.compile(
        r"\| `(?P<slug>[a-z0-9][a-z0-9-]*)` \| [^|]+ \| [^|]+ \| [^|]+ \|"
    )
    slugs = []
    for line in index_text.splitlines():
        if not line.startswith("| `"):
            continue
        match = row_pattern.fullmatch(line)
        if match is None:
            raise AssertionError(f"noncanonical skill index row: {line}")
        slugs.append(match.group("slug"))
    return slugs


def resolve_declared_source(root, source):
    source_path = Path(source)
    if source_path.is_absolute() or ".." in source_path.parts:
        raise ValueError(f"source path must stay repository-relative: {source}")
    resolved_root = root.resolve(strict=True)
    try:
        resolved = (resolved_root / source_path).resolve(strict=True)
        resolved.relative_to(resolved_root)
    except (FileNotFoundError, ValueError) as exc:
        raise ValueError(f"source path must resolve to an existing repository file: {source}") from exc
    if not resolved.is_file():
        raise ValueError(f"source path must resolve to an existing repository file: {source}")
    return resolved


class SkillsPackageStructureTests(unittest.TestCase):
    def test_package_scaffolding_exists(self):
        for relative in ("skills/README.md", "skills/INDEX.md", "skills/manifest.json"):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), f"missing {relative}")

    def test_installer_scripts_exist(self):
        for relative in ("scripts/install_skill.py", "scripts/install_skill.ps1"):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), f"missing {relative}")

    def test_catalog_contains_required_core_workflows(self):
        skill_slugs = {p.name for p in iter_skill_dirs()}
        self.assertTrue(
            REQUIRED_SKILL_SLUGS.issubset(skill_slugs),
            f"missing required skill(s): {sorted(REQUIRED_SKILL_SLUGS - skill_slugs)}",
        )


class SkillBundleContentTests(unittest.TestCase):
    def test_every_skill_has_required_frontmatter_and_sections(self):
        for skill_dir in iter_skill_dirs():
            skill_md = skill_dir / "SKILL.md"
            with self.subTest(skill=skill_dir.name):
                self.assertTrue(skill_md.is_file(), f"{skill_dir.name} has no SKILL.md")
                text = skill_md.read_text(encoding="utf-8")
                data, body = parse_frontmatter(text)

                for key in REQUIRED_FRONTMATTER_KEYS:
                    self.assertIn(key, data, f"{skill_dir.name} missing frontmatter key {key}")

                self.assertEqual(data.get("name"), skill_dir.name, f"{skill_dir.name} frontmatter name mismatch")
                self.assertIn(data.get("category"), ALLOWED_CATEGORIES, f"{skill_dir.name} has an unknown category")

                for section in REQUIRED_SECTIONS:
                    self.assertIn(section, body, f"{skill_dir.name} missing section {section}")

                self.assertTrue(text.endswith("\n"), f"{skill_dir.name} SKILL.md must end with a newline")

    def test_every_declared_source_path_exists(self):
        for skill_dir in iter_skill_dirs():
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            data, _ = parse_frontmatter(text)
            sources = data.get("source", [])
            self.assertTrue(sources, f"{skill_dir.name} declares no source paths")
            for source in sources:
                with self.subTest(skill=skill_dir.name, source=source):
                    resolved = resolve_declared_source(ROOT, source)
                    self.assertTrue(resolved.is_file())

    def test_declared_source_guard_rejects_absolute_traversal_and_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            safe = root / "docs" / "safe.md"
            safe.parent.mkdir()
            safe.write_text("safe\n", encoding="utf-8")
            self.assertEqual(safe.resolve(), resolve_declared_source(root, "docs/safe.md"))
            for invalid in (str(safe.resolve()), "../outside.md", "docs"):
                with self.subTest(source=invalid):
                    with self.assertRaisesRegex(ValueError, "repository-relative|repository file"):
                        resolve_declared_source(root, invalid)

    def test_no_skill_has_secret_looking_text(self):
        for skill_dir in iter_skill_dirs():
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=skill_dir.name):
                self.assertFalse(discover_ai_sources.has_secret_looking_text(text))

    def test_no_skill_has_generated_expansion_blocks(self):
        for skill_dir in iter_skill_dirs():
            relative = (skill_dir / "SKILL.md").relative_to(ROOT).as_posix()
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=skill_dir.name):
                self.assertEqual([], mechanical_research_expansion.audit_text(relative, text))

    def test_no_skill_uses_the_banned_hardware_phrase(self):
        for skill_dir in iter_skill_dirs():
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=skill_dir.name):
                self.assertNotIn("lightweight laptop", text.lower())

    def test_hermes_skills_stay_scoped_to_the_agent_tool(self):
        banned = re.compile(r"quantiz|GGUF|vLLM|SGLang|Ollama|model card|MMLU", re.IGNORECASE)
        allowed_context = re.compile(r"out of scope|do not|never|forbidden|exclude|not this", re.IGNORECASE)
        for skill_dir in iter_skill_dirs():
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            data, _ = parse_frontmatter(text)
            if data.get("category") != "hermes":
                continue
            for line in text.split("\n"):
                if banned.search(line):
                    with self.subTest(skill=skill_dir.name, line=line.strip()):
                        self.assertTrue(
                            allowed_context.search(line),
                            f"{skill_dir.name} may leak Hermes model/benchmark scope: {line.strip()}",
                        )


class SkillManifestAndIndexTests(unittest.TestCase):
    def test_manifest_matches_skill_directories_exactly(self):
        manifest = load_manifest()
        manifest_slug_sequence = [entry["slug"] for entry in manifest["skills"]]
        self.assertEqual([], duplicate_values(manifest_slug_sequence), "duplicate manifest skill slug")
        directory_slug_sequence = [p.name for p in iter_skill_dirs()]
        self.assertTrue(
            ordered_sequences_match(sorted(manifest_slug_sequence), directory_slug_sequence),
            "skills/manifest.json is out of sync with skills/",
        )

    def test_manifest_entries_have_required_fields(self):
        manifest = load_manifest()
        for entry in manifest["skills"]:
            with self.subTest(slug=entry.get("slug")):
                for key in ("slug", "description", "category", "source"):
                    self.assertIn(key, entry)
                self.assertIn(entry["category"], ALLOWED_CATEGORIES)
                self.assertIsInstance(entry["source"], list)
                self.assertTrue(entry["source"])

    def test_index_manifest_and_directories_have_exact_unique_skill_slugs(self):
        index_text = (SKILLS_DIR / "INDEX.md").read_text(encoding="utf-8")
        manifest = load_manifest()
        index_slug_sequence = parse_index_slugs(index_text)
        manifest_slug_sequence = [entry["slug"] for entry in manifest["skills"]]
        directory_slug_sequence = [path.name for path in iter_skill_dirs()]
        self.assertEqual([], duplicate_values(index_slug_sequence), "duplicate index skill slug")
        self.assertEqual([], duplicate_values(manifest_slug_sequence), "duplicate manifest skill slug")
        self.assertTrue(ordered_sequences_match(index_slug_sequence, manifest_slug_sequence))
        self.assertTrue(ordered_sequences_match(sorted(manifest_slug_sequence), directory_slug_sequence))

    def test_ordered_catalog_guard_detects_reordered_manifest_or_index(self):
        canonical = ["first", "second"]
        self.assertTrue(ordered_sequences_match(canonical, list(canonical)))
        self.assertFalse(ordered_sequences_match(canonical, list(reversed(canonical))))

    def test_duplicate_helpers_reject_manifest_and_canonical_index_duplicates(self):
        self.assertEqual(["dup"], duplicate_values(["dup", "unique", "dup"]))
        duplicate_index = (
            "| `dup` | guides | First row. | `docs/one.md` |\n"
            "| `dup` | guides | Second row. | `docs/two.md` |\n"
        )
        self.assertEqual(["dup", "dup"], parse_index_slugs(duplicate_index))
        self.assertEqual(["dup"], duplicate_values(parse_index_slugs(duplicate_index)))
        with self.assertRaisesRegex(AssertionError, "noncanonical skill index row"):
            parse_index_slugs("| `broken` | missing cells |\n")

    def test_manifest_source_guard_rejects_unsafe_or_nonregular_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", str(root)], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Skill Test"], check=True)
            subprocess.run(
                ["git", "-C", str(root), "config", "user.email", "skill-test@example.invalid"],
                check=True,
            )
            safe = root / "docs" / "safe.md"
            safe.parent.mkdir()
            safe.write_text("safe\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "docs/safe.md"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-m", "fixture"], check=True, capture_output=True)
            entries = git_tree_entries(root)

            committed_source_blob(root, "docs/safe.md", entries)
            for invalid in (str(safe.resolve()), "../outside.md", "missing.md", "docs"):
                with self.subTest(source=invalid):
                    with self.assertRaises(ValueError):
                        committed_source_blob(root, invalid, entries)

            nonregular = dict(entries)
            nonregular["docs/safe.md"] = {**entries["docs/safe.md"], "mode": "120000"}
            with self.assertRaisesRegex(ValueError, "regular Git blob"):
                committed_source_blob(root, "docs/safe.md", nonregular)

    def test_manifest_sources_must_match_skill_frontmatter_in_order(self):
        manifest_sources = ["docs/one.md", "docs/two.md"]
        self.assertTrue(ordered_sequences_match(manifest_sources, list(manifest_sources)))
        self.assertFalse(ordered_sequences_match(manifest_sources, list(reversed(manifest_sources))))
        self.assertFalse(ordered_sequences_match(manifest_sources, ["docs/other.md"]))

    def test_every_manifest_source_is_an_exact_head_blob_and_matches_frontmatter(self):
        manifest = load_manifest()
        entries = git_tree_entries(ROOT)
        for entry in manifest["skills"]:
            skill_text = (SKILLS_DIR / entry["slug"] / "SKILL.md").read_text(encoding="utf-8")
            frontmatter, _ = parse_frontmatter(skill_text)
            with self.subTest(slug=entry["slug"]):
                self.assertTrue(ordered_sequences_match(entry["source"], frontmatter["source"]))
            for source in entry["source"]:
                with self.subTest(slug=entry["slug"], source=source):
                    blob = committed_source_blob(ROOT, source, entries)
                    self.assertEqual(entries[source]["sha256"], hashlib.sha256(blob).hexdigest())


class SkillInstallerBehaviorTests(unittest.TestCase):
    def run_installer(self, args, cwd):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "install_skill.py"), *args],
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_python_installer_can_install_every_skill_for_native_harness(self):
        manifest = load_manifest()
        native_cases = {
            "claude-code-cli": Path(".claude") / "skills",
            "claude-code-desktop": Path(".claude") / "skills",
            "codex-cli": Path(".agents") / "skills",
            "codex-desktop": Path(".agents") / "skills",
        }
        for harness, target_root in native_cases.items():
            with self.subTest(harness=harness), tempfile.TemporaryDirectory() as tmp:
                result = self.run_installer(["--all", "--harness", harness], tmp)

                self.assertEqual(result.returncode, 0, result.stderr)
                for entry in manifest["skills"]:
                    slug = entry["slug"]
                    skill_path = Path(tmp) / target_root / slug / "SKILL.md"
                    with self.subTest(harness=harness, slug=slug):
                        self.assertTrue(skill_path.is_file(), f"{slug} was not installed")
                        text = skill_path.read_text(encoding="utf-8")
                        self.assertTrue(text.startswith("---\n"), f"{slug} lost frontmatter")
                        self.assertIn(f"name: {slug}", text)

    def test_python_installer_can_stage_every_skill_for_non_native_harness(self):
        manifest = load_manifest()
        with tempfile.TemporaryDirectory() as tmp:
            result = self.run_installer(["--all", "--harness", "cursor"], tmp)

            self.assertEqual(result.returncode, 0, result.stderr)
            for entry in manifest["skills"]:
                slug = entry["slug"]
                skill_path = Path(tmp) / ".agent-skills" / "cursor" / f"{slug}.md"
                with self.subTest(slug=slug):
                    self.assertTrue(skill_path.is_file(), f"{slug} was not staged")
                    text = skill_path.read_text(encoding="utf-8")
                    self.assertFalse(text.startswith("---\n"), f"{slug} still has frontmatter")
                    self.assertIn("## Trigger", text)

    def test_python_installer_can_stage_hermes_project_skills(self):
        manifest = load_manifest()
        with tempfile.TemporaryDirectory() as tmp:
            result = self.run_installer(["--all", "--harness", "hermes"], tmp)

            self.assertEqual(result.returncode, 0, result.stderr)
            for entry in manifest["skills"]:
                slug = entry["slug"]
                skill_path = Path(tmp) / ".agent-skills" / "hermes" / slug / "SKILL.md"
                with self.subTest(slug=slug):
                    self.assertTrue(skill_path.is_file(), f"{slug} was not staged for Hermes")
                    text = skill_path.read_text(encoding="utf-8")
                    self.assertTrue(text.startswith("---\n"), f"{slug} lost frontmatter")
                    self.assertIn(f"name: {slug}", text)

    def test_installer_harnesses_cover_requested_surfaces(self):
        requested = {
            "codex-cli",
            "codex-desktop",
            "claude-code-cli",
            "claude-code-desktop",
            "hermes",
        }
        self.assertTrue(requested.issubset(set(install_skill.ALL_HARNESSES)))

        ps1_text = (SCRIPTS / "install_skill.ps1").read_text(encoding="utf-8")
        for harness in requested:
            with self.subTest(harness=harness):
                self.assertIn(f'"{harness}"', ps1_text)

    def test_skill_install_docs_do_not_use_placeholder_setup_language(self):
        paths = [
            ROOT / "README.md",
            ROOT / "docs" / "skills" / "codex.md",
            ROOT / "skills" / "README.md",
        ]
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                text = path.read_text(encoding="utf-8").lower()
                self.assertNotIn("placeholder only", text)
                self.assertNotIn("publish placeholders only", text)

    def test_codex_docs_use_current_agents_skill_path(self):
        paths = [
            ROOT / "README.md",
            ROOT / "docs" / "skills" / "codex.md",
            ROOT / "skills" / "README.md",
        ]
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                text = path.read_text(encoding="utf-8")
                self.assertIn(".agents/skills", text)
                self.assertNotIn(".codex/skills", text)

    def test_meta_skills_support_self_extension_and_self_prompts(self):
        create_text = (SKILLS_DIR / "create-a-new-skill" / "SKILL.md").read_text(encoding="utf-8")
        runner_text = (SKILLS_DIR / "self-directed-goal-runner" / "SKILL.md").read_text(encoding="utf-8")
        install_text = (SKILLS_DIR / "install-this-skill-pack" / "SKILL.md").read_text(encoding="utf-8")

        for expected in ("prompting skill", "skills/INDEX.md", "skills/manifest.json", "not just a title"):
            with self.subTest(skill="create-a-new-skill", expected=expected):
                self.assertIn(expected, create_text)

        for expected in (".tmp/self-prompts", "checklist", "iteration cap", "stop condition"):
            with self.subTest(skill="self-directed-goal-runner", expected=expected):
                self.assertIn(expected, runner_text)

        for expected in ("codex-cli", "codex-desktop", "claude-code-cli", "claude-code-desktop", "hermes"):
            with self.subTest(skill="install-this-skill-pack", expected=expected):
                self.assertIn(expected, install_text)


if __name__ == "__main__":
    unittest.main()
