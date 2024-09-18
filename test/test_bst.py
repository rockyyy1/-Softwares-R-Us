import unittest
import random
from app.player_bst import PlayerBST, create_balanced_bst
from app.player import Player


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()
        self.player1 = Player(uid = "001", player_name= "Bulbasaur")
        self.player2 = Player(uid = "002", player_name= "Ivysaur")
        self.player3 = Player(uid = "003", player_name= "Venasaur")
        self.player4 = Player(uid = "004", player_name= "Charmander")
        self.player5 = Player(uid="063", player_name="Abra")
        self.player6 = Player(uid="025", player_name="Pikachu")
        self.player7 = Player(uid="007", player_name="Squirtle")
        self.player8 = Player(uid="008", player_name="Wartortle")

    def test_insert_empty(self):
        self.bst.insert(player = self.player1)
        self.assertEqual(self.bst.root.player, self.player1)

    def test_insert_left(self):
        self.bst.insert(player = self.player4)
        self.bst.insert(player = self.player1)
        self.assertEqual(self.bst.root.player, self.player4)
        self.assertEqual(self.bst.root.left.player, self.player1)

    def test_insert_right(self):
        self.bst.insert(player = self.player4)
        self.bst.insert(player = self.player1)
        self.bst.insert(player = self.player3)
        self.assertEqual(self.bst.root.player, self.player4)
        self.assertEqual(self.bst.root.left.player, self.player1)
        self.assertEqual(self.bst.root.right.player, self.player3)

    def test_insert_existing(self):
        self.bst.insert(player = self.player4)
        self.bst.insert(player = self.player1)
        self.bst.insert(player = self.player3)
        player5 = Player(uid = "test", player_name = "Bulbasaur")
        self.bst.insert(player = player5)
        self.assertEqual(self.bst.root.left.player, player5)

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
        self.bst.insert(Player(uid="008", player_name="wartortle"))
        self.bst.insert(self.player1)
        self.bst.insert(Player(uid="063", player_name="Abra"))
        self.bst.insert(self.player2)
        self.bst.insert(Player(uid="025", player_name="pikachu"))
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)

        sorted_nodes = self.bst.sort_nodes_to_list()
        shuffled_list = sorted_nodes.copy()
        random.shuffle(shuffled_list)
        self.assertEqual(sorted_nodes, sorted(shuffled_list))

    def test_create_balanced_bst(self):
        self.bst.insert(self.player1)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)
        self.bst.insert(self.player5)
        self.bst.insert(self.player6)
        self.bst.insert(self.player7)
        self.bst.insert(self.player8)
        rocky = Player(uid="069", player_name="Rocky")
        self.bst.insert(rocky)

        sorted_nodes = self.bst.sort_nodes_to_list()
        # print(sorted_nodes)
        balanced_bst = create_balanced_bst(sorted_nodes)
        middle_index = len(sorted_nodes) // 2

        #root is the middle of the list
        self.assertEqual(balanced_bst.root, sorted_nodes[middle_index])

        #left subtree
        left_subtree = sorted_nodes[:middle_index]
        left_subtree_middle_index = len(left_subtree) // 2
        self.assertEqual(balanced_bst.root.left, left_subtree[left_subtree_middle_index])

        #right subtree
        right_subtree = sorted_nodes[middle_index+1:]
        right_subtree_middle = len(right_subtree) // 2
        self.assertEqual(balanced_bst.root.right, right_subtree[right_subtree_middle])


