
import unittest

from app.hash_map import PlayerHashMap, Player

class HashTest(unittest.TestCase):
    def test_initialize_hashmap(self):
        player_table = PlayerHashMap()
        self.assertEqual(player_table.SIZE, 10)

    def test_size(self):
        player_table = PlayerHashMap()
        player_table.put(key="1", name='Rocky')
        self.assertEqual(player_table.size(), 1)

    def test_hash_determinism(self):
        player_table = PlayerHashMap()
        player_1 = Player("123", "Rocky")
        hash_1 = hash(player_1)
        hash_2 = hash(player_1)
        self.assertEqual(hash_1 , hash_2)

    def test_get_index_string(self):
        player_table = PlayerHashMap()
        for i in range(100):
            index = player_table.get_index(str(i))
            #print(index)
            self.assertLess(index, player_table.SIZE)

    def test_get_index_Player(self):
        player_table = PlayerHashMap()
        player_1 = Player(uid ="123", player_name="Rocky")
        index = player_table.get_index(key = player_1)
        self.assertLess(index, player_table.SIZE)

    def test_eq_player_uid(self):
        player_table = PlayerHashMap()
        player_table.put(key = "1", name = "Rocky")
        player_1 = Player(uid = "1", player_name = "Raf")
        self.assertEqual(player_table.get(key = "1"), player_1)

    def test_put_empty_string(self):
        player_table = PlayerHashMap()
        with self.assertRaises(ValueError):
            player_table.put(key="", name="rocky")

    def test_put_collision_handling(self):
        player_table = PlayerHashMap()
        player_table.put(key = "3", name = "Rocky")
        player_table.put(key="4", name="Rocky")
        self.assertEqual(player_table.get_index(key = "3"), player_table.get_index(key = "4"))
        self.assertEqual(player_table.size(), 2)

    def test_put_duplicate_key(self):
        player_table = PlayerHashMap()
        player_table.put(key="1", name="Raf")
        player_table.put(key="5", name="Kyle")
        player_table.put(key="5", name="Homer")
        player_table.put(key="5", name="Sebastian")
        player_table.put(key="5", name="Updated")
        self.assertEqual(player_table.size(), 2)
        self.assertEqual(player_table.get(key = "5").name, "Updated")

    def test_get_no_key_found(self):
        player_table = PlayerHashMap()
        player_table.put(key="1", name = "Rocky")
        with self.assertRaises(KeyError):
            player_table.get(key="2")

    def test_get_on_empty_hashmap(self):
        player_table = PlayerHashMap()
        with self.assertRaises(KeyError):
            player_table.get(key="1")

    def test_get(self):
        player_table = PlayerHashMap()
        player_table.put(key = "123abc!@#", name = "Rocky")
        player_table.put(key="1", name="Raf")
        player_table.put(key="5", name="Murray")
        player_table.put(key="5", name="John")
        player_table.put(key="7", name="James")
        player_table.put(key="7", name="Kai")
        player_table.put(key="7", name="Raf")
        player_table.put(key="7", name="Sebastian")
        self.assertEqual(player_table.get(key ="7").name, "Sebastian")
        self.assertEqual(player_table.get(key ="123abc!@#").name, "Rocky")
        self.assertEqual(player_table.get(key ="5").name, "John")

    def test_remove_key_not_found(self):
        player_table = PlayerHashMap()
        player_table.put(key="1", name="Rocky")
        with self.assertRaises(KeyError):
            player_table.remove(key="2")

    def test_remove(self):
        player_table = PlayerHashMap()
        player_table.put(key= "1", name="Rocky")
        player_table.put(key="2", name="Raf")
        player_table.put(key="3", name="Murray")
        player_table.put(key="4", name="John")
        player_table.put(key="5", name="James")
        player_table.put(key="6", name="Kai")
        player_table.put(key="7", name="Raf")
        player_table.put(key="7", name="Sebastian")
        player_table.remove("7")
        self.assertEqual(player_table.size(), 6)
        with self.assertRaises(KeyError):
            player_table.get(key='7')

    def test_display(self):
        player_table = PlayerHashMap()
        hashed_value = 0
        for i in range(10):
            player_table.put(key = str(i), name = "Random Name")
            hashed_value += 1
        player_table.display()
        self.assertEqual(player_table.size(), 10)

