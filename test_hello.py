import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_greet_codex(self):
        self.assertEqual(greet("Codex"), "Hello, Codex!")


if __name__ == "__main__":
    unittest.main()
