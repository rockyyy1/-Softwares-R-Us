from app.player import Player
import unittest
import random

# Resources:
# https://docs.python-guide.org/writing/tests/

class MyTest(unittest.TestCase):
    def test_uid(self):
        p1 = Player("123456", "Rocky")
        self.assertEqual(p1.uid, "123456")

    def test_name(self):
        p2 = Player("45", "Adam")
        self.assertEqual(p2.name, "Adam")

    def test_score_getter(self):
        p1 = Player("123456", "Rocky")
        self.assertEqual(p1.score, 0)

    def test_score_setter(self):
        p1 = Player("123456", "Rocky")
        p1.score = 169
        self.assertEqual(p1.score, 169)

    def test_score_setter_negative(self):
        p1 = Player("123456", "Rocky")
        with self.assertRaises(ValueError):
            p1.score = -13

    def test_score_setter_invalid_type(self):
        p1 = Player("123456", "Rocky")
        with self.assertRaises(TypeError):
            p1.score = "hello"
        with self.assertRaises(TypeError):
            p1.score = None

    def test_eq(self):
        p1 = Player("123456", "Rocky")
        p2 = Player("45", "Adam")
        p2.score = 1
        p1.score = 1
        self.assertTrue(p1, p2)
        self.assertTrue(p1 == p2)

    def test_eq_different_types(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        self.assertFalse(p1 == "1")
        self.assertFalse(p1 == "hello")
        self.assertFalse(p1 == [1,2,3])

    def test_eq_integer(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        self.assertTrue(p1 == 1)
        self.assertFalse(p1 == 2)

    def test_lt(self):
        p1 = Player("123456", "Rocky")
        p2 = Player("45", "Adam")
        p1.score = 1
        p2.score = 2
        self.assertTrue(p1 < p2)

    def test_lt_different_types(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        with self.assertRaises(TypeError):
            result = p1 < "hello"
        with self.assertRaises(TypeError):
            result = p1 < [1, 2, 3]

    def test_lt_integer(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        self.assertTrue(p1 < 10)
        self.assertFalse(p1 < 1)

    def test_le(self):
        p1 = Player("123456", "Rocky")
        p2 = Player("45", "Adam")
        p1.score = 1
        p2.score = 2
        self.assertTrue(p1 <= p2)
        p1.score = 2
        self.assertTrue(p1 <= p2)

    def test_le_different_types(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        with self.assertRaises(TypeError):
            result = p1 <= "hello"
        with self.assertRaises(TypeError):
            result = p1 <= [1, 2, 3]

    def test_le_integer(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        self.assertTrue(p1 <= 10)
        self.assertTrue(p1 <= 1)
        self.assertFalse(p1 <= 0)

    def test_gt(self):
        p1 = Player("123456", "Rocky")
        p2 = Player("45", "Adam")
        p1.score = 2
        p2.score = 1
        self.assertTrue(p1 > p2)

    def test_gt_different_types(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        with self.assertRaises(TypeError):
            result = p1 > "hello"
        with self.assertRaises(TypeError):
            result = p1> [1, 2, 3]

    def test_gt_integer(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        self.assertTrue(p1 > 0)
        self.assertFalse(p1 > 10)

    def test_ge(self):
        p1 = Player("123456", "Rocky")
        p2 = Player("45", "Adam")
        p1.score = 2
        p2.score = 1
        self.assertTrue(p1 >= p2)
        p1.score = 1
        self.assertTrue(p1 >= p2)

    def test_ge_different_types(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        with self.assertRaises(TypeError):
            result = p1 > "hello"
        with self.assertRaises(TypeError):
            result = p1> [1, 2, 3]

    def test_ge_integer(self):
        p1 = Player("123456", "Rocky")
        p1.score = 10
        self.assertTrue(p1 >= 5)
        self.assertTrue(p1 >= 10)
        self.assertFalse(p1 >= 20)

    def test_ne(self):
        p1 = Player("123456", "Rocky")
        p2 = Player("45", "Adam")
        p1.score = 1
        p2.score = 2
        self.assertTrue(p1 != p2)
        p2.score = 1
        self.assertFalse(p1 != p2)

    def test_ne_different_types(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        self.assertTrue(p1 != "1")
        self.assertTrue(p1 != "hello")
        self.assertTrue(p1 != [1,2,3])

    def test_ne_integer(self):
        p1 = Player("123456", "Rocky")
        p1.score = 1
        self.assertFalse(p1 != 1)
        self.assertTrue(p1 != 2)

    def test_sort_empty_list(self):
        some_list = []
        quick_sort = Player.sort_players_by_score(some_list)
        python_sort = sorted(some_list)
        self.assertEqual(quick_sort, python_sort)

    def test_sort_single_player(self):
        p1 = Player("123456", "Rocky")
        quick_sort = Player.sort_players_by_score([p1])
        python_sort = sorted([p1])
        self.assertEqual(quick_sort, python_sort)

    def test_sort_players_by_score(self):
        p1 = Player("123456", "Rocky")
        p2 = Player("009", "Blastoise")
        p3 = Player("003", "Venusaur")
        p4 = Player("006", "Charizard")
        p1.score = 56
        p2.score = 22
        p3.score = 25
        p4.score = 1
        players = [p1, p2, p3, p4]
        quick_sort = Player.sort_players_by_score(players)
        python_sort = sorted(players, reverse = True)
        self.assertEqual(quick_sort, python_sort)

    def test_sort_large_list(self):
        players = []
        for i in range(100):
            player = Player(f"{i}", f"Player #{i}")
            player.score = random.randint(1, 100)
            players.append(player)
        quick_sort = Player.sort_players_by_score(players)
        python_sort = sorted(players, reverse=True)
        self.assertEqual(quick_sort, python_sort)