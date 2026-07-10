import unittest

from scripts.strip_research_expansion import strip_blocks

MD = (
    "# Title\n\nReal content.\n\n"
    "<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->\n"
    "filler line\n"
    "<!-- RESEARCH-GRADE-EXPANSION:END -->\n"
)

PY = (
    "print('hi')\n\n"
    "# RESEARCH-GRADE-EXPANSION:BEGIN\n"
    "# notes\n"
    "# RESEARCH-GRADE-EXPANSION:END\n"
)

QUOTED = 'MARKER_BEGIN = "RESEARCH-GRADE-EXPANSION:BEGIN"\nMARKER_END = "RESEARCH-GRADE-EXPANSION:END"\n'


class StripBlocksTest(unittest.TestCase):
    def test_strips_markdown_block(self) -> None:
        text, removed = strip_blocks(MD)
        self.assertEqual(removed, 1)
        self.assertEqual(text, "# Title\n\nReal content.\n")

    def test_strips_hash_comment_block(self) -> None:
        text, removed = strip_blocks(PY)
        self.assertEqual(removed, 1)
        self.assertEqual(text, "print('hi')\n")

    def test_leaves_quoted_markers_alone(self) -> None:
        text, removed = strip_blocks(QUOTED)
        self.assertEqual(removed, 0)
        self.assertEqual(text, QUOTED)

    def test_unclosed_block_untouched(self) -> None:
        broken = "a\n<!-- RESEARCH-GRADE-EXPANSION:BEGIN -->\nb\n"
        text, removed = strip_blocks(broken)
        self.assertEqual(removed, 0)
        self.assertEqual(text, broken)

    def test_idempotent(self) -> None:
        once, _ = strip_blocks(MD)
        twice, removed = strip_blocks(once)
        self.assertEqual(removed, 0)
        self.assertEqual(twice, once)


if __name__ == "__main__":
    unittest.main()
