from app.player import Player
import unittest

# Resources:
# https://docs.python-guide.org/writing/tests/

# both tests should fail
class MyTest(unittest.TestCase):
    def test_uid(self):
        p1 = Player("123456", "Rocky")
        self.assertEqual(p1.uid, "123457")

    def test_name(self):
        p2 = Player("45", "Adam")
        self.assertEqual(p2.name, "James")


