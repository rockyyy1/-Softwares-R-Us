from app.player import Player
from app.player_list import PlayerList

import unittest

from app.player_node import PlayerNode


# Resources:
# https://docs.python-guide.org/writing/tests/

p1 = Player("123", "Rocky")
p2 = Player("456", "Raf")

class MyTest(unittest.TestCase):
    def test_return_true_if_empty(self):
        l1 =  PlayerList()
        self.assertTrue(l1.is_empty)

    def test_add_to_empty_list(self):
        l2 = PlayerList()
        print(l2.is_empty)
        l2.insert_at_head(PlayerNode(p1))
        print(l2.is_empty)
        self.assertFalse(l2.is_empty)

    def test_add_to_not_empty_list(self):
        l3 = PlayerList()
        print(l3.is_empty)
        l3.insert_at_head(PlayerNode(p1))
        print(l3.is_empty)
        l3.insert_at_head(PlayerNode(p2))
        print(l3.is_empty)
        self.assertFalse(l3.is_empty)

    def test_return_head_node(self):
        l1 = PlayerList()
        l1.insert_at_head(PlayerNode(p1))
        l1.insert_at_head(PlayerNode(p2))
        self.assertEqual(l1.head.player, p2)

    def test_return_tail_node(self):
        l1 = PlayerList()
        l1.insert_at_head(PlayerNode(p1))
        l1.insert_at_head(PlayerNode(p2))
        self.assertEqual(l1.tail.player, p1)

