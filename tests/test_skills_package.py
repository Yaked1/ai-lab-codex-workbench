"""Tests for the skills/ package: every skill bundle, the manifest, the
index, and both installer scripts.

These guards keep every skill honest about what it claims to summarize: a
skill can never silently drift from the guide it packages, because its
declared `source` paths are checked against the real file tree on every
run, and it can never go missing from the installer's manifest without the
test suite noticing.
"""
import importlib.util
import json
import re
import sys
import unittest
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

STARTER_SKILL_SLUGS = {
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


class SkillsPackageStructureTests(unittest.TestCase):
    def test_package_scaffolding_exists(self):
        for relative in ("skills/README.md", "skills/INDEX.md", "skills/manifest.json"):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), f"missing {relative}")

    def test_installer_scripts_exist(self):
        for relative in ("scripts/install_skill.py", "scripts/install_skill.ps1"):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), f"missing {relative}")

    def test_starter_pack_contains_expected_skills(self):
        skill_slugs = {p.name for p in iter_skill_dirs()}
        self.assertTrue(
            STARTER_SKILL_SLUGS.issubset(skill_slugs),
            f"missing starter skill(s): {sorted(STARTER_SKILL_SLUGS - skill_slugs)}",
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
                    self.assertTrue((ROOT / source).exists(), f"{skill_dir.name} points at missing file {source}")

    def test_no_skill_has_secret_looking_text(self):
        for skill_dir in iter_skill_dirs():
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=skill_dir.name):
                self.assertFalse(discover_ai_sources.has_secret_looking_text(text))

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
        manifest_slugs = {entry["slug"] for entry in manifest["skills"]}
        directory_slugs = {p.name for p in iter_skill_dirs()}

        self.assertEqual(manifest_slugs, directory_slugs, "skills/manifest.json is out of sync with skills/")

    def test_manifest_entries_have_required_fields(self):
        manifest = load_manifest()
        for entry in manifest["skills"]:
            with self.subTest(slug=entry.get("slug")):
                for key in ("slug", "description", "category", "source"):
                    self.assertIn(key, entry)
                self.assertIn(entry["category"], ALLOWED_CATEGORIES)
                self.assertIsInstance(entry["source"], list)
                self.assertTrue(entry["source"])

    def test_index_lists_every_skill(self):
        index_text = (SKILLS_DIR / "INDEX.md").read_text(encoding="utf-8")
        manifest = load_manifest()
        for entry in manifest["skills"]:
            with self.subTest(slug=entry["slug"]):
                self.assertIn(entry["slug"], index_text, f"{entry['slug']} missing from skills/INDEX.md")


if __name__ == "__main__":
    unittest.main()
