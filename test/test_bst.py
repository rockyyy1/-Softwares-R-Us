import unittest
import random

from app.player_bnode import PlayerBNode
from app.player_bst import PlayerBST
from app.player import Player


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()
        self.player1 = Player(uid = "001", player_name= "Bulbasaur")
        self.player2 = Player(uid = "002", player_name= "Ivysaur")
        self.player3 = Player(uid = "003", player_name= "Venasaur")
        self.player4 = Player(uid = "004", player_name= "Charmander")

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

    def test_insert_existing(self):
        self.bst.insert(player = self.player4)
        self.bst.insert(player = self.player1)
        self.bst.insert(player = self.player3)
        player5 = Player(uid = "test", player_name = "Bulbasaur")
        self.bst.insert(player = player5)
        self.assertEqual(self.bst.root.left._player, player5)

    def test_multiple(self):
        players = [self.player1, self.player2, self.player3, self.player4]
        for player in players:
            self.bst.insert(player)
        self.assertEqual(self.bst.root.player, self.player1)
        self.assertEqual(self.bst.root.right.player, self.player4)
        self.assertEqual(self.bst.root.right.left.player, self.player3)
        self.assertEqual(self.bst.root.right.right.player, self.player1)

    def test_search_empty_bst(self):
        self.assertEqual(self.bst.search(name = "Bulbasaur"), None)

    def test_search(self):
        self.bst.insert(player = self.player1)
        self.bst.insert(player = self.player2)
        self.bst.insert(player = self.player3)
        self.assertEqual(self.bst.search("Bulbasaur"), self.player1)
        self.assertEqual(self.bst.search("IvYsAuR"), self.player2)
        self.assertEqual(self.bst.search("VENASAUR"), self.player3)

    def test_search_not_found(self):
        self.bst.insert(player = self.player1)
        self.assertIsNone(self.bst.search("Pikachu"))
        self.assertEqual(self.bst.search("Squirtle"), None)

    def test_sorted_list(self):
        self.bst.insert(self.player1)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)
        self.bst.insert(Player(uid="063", player_name="Abra"))

        sorted_nodes = self.bst.sort_list()
        sorted_names = [node.player.player_name for node in sorted_nodes]
        self.assertEqual(sorted_names, sorted(sorted_names))

    def test_create_balanced_bst(self):
        self.bst.insert(self.player1)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)
        self.bst.insert(Player(uid="063", player_name="Abra"))
        self.player5 = Player(uid="025", player_name="Pikachu")
        self.player6 = Player(uid="007", player_name="Squirtle")
        self.player7 = Player(uid="008", player_name="Wartortle")




