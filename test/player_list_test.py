from app.player import Player
from app.player_list import PlayerList

import unittest

from app.player_node import PlayerNode


# Resources:
# https://docs.python-guide.org/writing/tests/

player_1 = Player("123", "Rocky")
player_2 = Player("456", "Raf")
player_3 = Player("789", "Murray")

class MyTest(unittest.TestCase):
    def test_return_true_if_empty(self):
        lst =  PlayerList()
        self.assertTrue(lst.is_empty)

    def test_add_to_head_empty_list(self):
        lst = PlayerList()
        print(lst.is_empty)
        lst.insert_at_head(PlayerNode(player_1))
        print(lst.is_empty)
        self.assertFalse(lst.is_empty)

    def test_add_to_head_not_empty_list(self):
        lst = PlayerList()
        print(lst.is_empty)
        lst.insert_at_head(PlayerNode(player_1))
        print(lst.is_empty)
        lst.insert_at_head(PlayerNode(player_2))
        print(lst.is_empty)
        self.assertFalse(lst.is_empty)

    def test_return_head_node(self):
        lst = PlayerList()
        lst.insert_at_head(PlayerNode(player_1))
        lst.insert_at_head(PlayerNode(player_2))
        self.assertEqual(lst.head.player, player_2)

    def test_return_tail_node(self):
        lst = PlayerList()
        lst.insert_at_head(PlayerNode(player_1))
        lst.insert_at_head(PlayerNode(player_2))
        self.assertEqual(lst.tail.player, player_1)

    def test_add_to_tail_empty_list(self):
        lst = PlayerList()
        lst.insert_at_tail(PlayerNode(player_1))
        self.assertEqual(lst.tail.player, player_1)

    def test_add_to_tail_not_empty_list(self):
        lst = PlayerList()
        lst.insert_at_tail(PlayerNode(player_1))
        lst.insert_at_tail(PlayerNode(player_2))
        self.assertEqual(lst.tail.player, player_2)

# Unit testing with Exceptions Resource:
# https://www.geeksforgeeks.org/test-if-a-function-throws-an-exception-in-python/
    def test_delete_head_node_on_empty_list(self):
        lst = PlayerList()
        with self.assertRaises(IndexError):
            lst.delete_from_head()

    def test_delete_tail_node_on_empty_list(self):
        lst = PlayerList()
        with self.assertRaises(IndexError):
            lst.delete_from_tail()

    def test_delete_head_node(self):
        lst = PlayerList()
        lst.insert_at_head(PlayerNode(player_1))
        lst.insert_at_head(PlayerNode(player_2))
        lst.insert_at_head(PlayerNode(player_3))
        lst.delete_from_head()
        self.assertEqual(lst.head.player, player_2)

    def test_delete_tail_node(self):
        lst = PlayerList()
        lst.insert_at_tail(PlayerNode(player_3))
        lst.insert_at_head(PlayerNode(player_2))
        lst.insert_at_tail(PlayerNode(player_1))
        lst.delete_from_tail()
        self.assertEqual(lst.tail.player, player_3)

    def test_deleting_key_empty_list(self):
        lst = PlayerList()
        with self.assertRaises(KeyError):
            lst.delete_key("123")

    def test_deleting_key_no_key_found(self):
        lst = PlayerList()
        lst.insert_at_head(PlayerNode(player_1))
        lst.insert_at_head(PlayerNode(player_2))
        with self.assertRaises(KeyError):
            lst.delete_key("blahblahblah")

    def test_deleting_key(self):
        lst = PlayerList()
        lst.insert_at_head(PlayerNode(player_1))
        lst.insert_at_head(PlayerNode(player_2))
        lst.insert_at_head(PlayerNode(player_3))
        lst.delete_key("789")
        self.assertEqual(lst.head.player, player_2)

    def test_display_empty(self):
        lst = PlayerList()
        expected_string = "List is empty"
        self.assertEqual(lst.display(forward = True), expected_string)


    def test_display_forward(self):
        lst = PlayerList()
        lst.insert_at_head(PlayerNode(player_1))
        lst.insert_at_head(PlayerNode(player_2))
        lst.insert_at_head(PlayerNode(player_3))
        expected_string = "Head -> Tail\nMurray -> Raf -> Rocky"
        self.assertEqual(lst.display(forward = True), expected_string)

    def test_display_backwards(self):
        lst = PlayerList()
        lst.insert_at_head(PlayerNode(player_1))
        lst.insert_at_head(PlayerNode(player_2))
        lst.insert_at_head(PlayerNode(player_3))
        expected_string = "Tail -> Head\nRocky -> Raf -> Murray"
        self.assertEqual(lst.display(forward = False), expected_string)