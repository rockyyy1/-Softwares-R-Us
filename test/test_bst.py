import unittest
import random

from app.player_bnode import PlayerBNode
from app.player_bst import PlayerBST, is_valid_bst
from app.player import Player


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()
        self.player1 = Player(uid = "001", player_name= "Bulbasaur")
        self.player4 = Player(uid = "004", player_name= "Charmander")
        self.player2 = Player(uid = "002", player_name= "Ivysaur")
        self.player3 = Player(uid = "003", player_name= "Venasaur")

    def test_insert_empty(self):
        self.bst.insert(player = self.player1)
        self.assertEqual(self.bst.root._player, self.player1)

    def test_insert_left(self):
        self.bst.insert(player = self.player4)
        self.bst.insert(player = self.player1)
        self.assertEqual(self.bst.root._player, self.player4)
        self.assertEqual(self.bst.root.left._player, self.player1)

    def test_insert_right(self):
        self.bst.insert(player = self.player4)
        self.bst.insert(player = self.player1)
        self.bst.insert(player = self.player3)
        self.assertEqual(self.bst.root._player, self.player4)
        self.assertEqual(self.bst.root.left._player, self.player1)
        self.assertEqual(self.bst.root.right._player, self.player3)

    def test_multiple(self):
        players = [self.player1, self.player2, self.player3, self.player4]
        for player in players:
            self.bst.insert(player)
        self.assertEqual(self.bst.root._player, self.player1)
        self.assertEqual(self.bst.root.right._player, self.player4)
        self.assertEqual(self.bst.root.right.left._player, self.player3)
        self.assertEqual(self.bst.root.right.right._player, self.player1)

    def test_subtrees_are_BST(self):
        players = [Player(f"{i}", f"Player #{i}") for i in range(100)]
        for player in players:
            self.bst.insert(player)
            # print(player.player_name)
        self.assertTrue(is_valid_bst(node = self.bst.root))
        self.assertTrue(is_valid_bst(node = self.bst.root.right))
        self.assertTrue(is_valid_bst(node = self.bst.root.left))

