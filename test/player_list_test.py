from app.player import Player
from app.player_list import PlayerList

import unittest

from app.player_node import PlayerNode


# Resources:
# https://docs.python-guide.org/writing/tests/

p1 = Player("123", "Rocky")
p2 = Player("456", "Raf")
p3 = Player("789", "Murray")

class MyTest(unittest.TestCase):
    def test_return_true_if_empty(self):
        l1 =  PlayerList()
        self.assertTrue(l1.is_empty)

    def test_add_to_head_empty_list(self):
        l2 = PlayerList()
        print(l2.is_empty)
        l2.insert_at_head(PlayerNode(p1))
        print(l2.is_empty)
        self.assertFalse(l2.is_empty)

    def test_add_to_head_not_empty_list(self):
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

    def test_add_to_tail_empty_list(self):
        l1 = PlayerList()
        l1.insert_at_tail(PlayerNode(p1))
        self.assertEqual(l1.tail.player, p1)

    def test_add_to_tail_not_empty_list(self):
        l1 = PlayerList()
        l1.insert_at_tail(PlayerNode(p1))
        l1.insert_at_tail(PlayerNode(p2))
        self.assertEqual(l1.tail.player, p2)

# Unit testing with Exceptions Resource:
# https://www.geeksforgeeks.org/test-if-a-function-throws-an-exception-in-python/
    def test_delete_head_node_on_empty_list(self):
        l1 = PlayerList()
        with self.assertRaises(IndexError):
            l1.delete_from_head()

    def test_delete_tail_node_on_empty_list(self):
        l1 = PlayerList()
        with self.assertRaises(IndexError):
            l1.delete_from_tail()

    def test_delete_head_node(self):
        l1 = PlayerList()
        l1.insert_at_head(PlayerNode(p1))
        l1.insert_at_head(PlayerNode(p2))
        l1.insert_at_head(PlayerNode(p3))
        l1.delete_from_head()
        self.assertEqual(l1.head.player, p2)

    def test_delete_tail_node(self):
        l1 = PlayerList()
        l1.insert_at_tail(PlayerNode(p3))
        l1.insert_at_head(PlayerNode(p2))
        l1.insert_at_tail(PlayerNode(p1))
        l1.delete_from_tail()
        self.assertEqual(l1.tail.player, p3)

    def test_deleting_key_empty_list(self):
        l1 = PlayerList()
        with self.assertRaises(IndexError):
            l1.delete_key("123")

    def test_deleting_key_no_key_found(self):
        l1 = PlayerList()
        l1.insert_at_head(PlayerNode(p1))
        l1.insert_at_head(PlayerNode(p2))
        with self.assertRaises(ValueError):
            l1.delete_key("blahblahblah")

    def test_deleting_key(self):
        l1 = PlayerList()
        l1.insert_at_head(PlayerNode(p1))
        l1.insert_at_head(PlayerNode(p2))
        l1.insert_at_head(PlayerNode(p3))
        l1.delete_key("789")
        self.assertEqual(l1.head.player, p2)
