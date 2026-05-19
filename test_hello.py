import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_greet_codex(self):
        self.assertEqual(greet("Codex"), "Hello, Codex!")

    def test_greet_xiaoming(self):
        self.assertEqual(greet("小明"), "你好，小明！")


if __name__ == "__main__":
    unittest.main()
