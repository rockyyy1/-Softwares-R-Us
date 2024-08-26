from __future__ import annotations

from player_list import PlayerList
from player import Player
from  player_node import PlayerNode


class PlayerHashMap:
    """A hash map of PlayerLists to store and manage Players.

    Attributes:
        SIZE (int): The number of PlayerLists in the hash map.
        hashmap (list): A list of PlayerList objects
    """
    def __init__(self):
        self.SIZE = 10
        self.hashmap = [PlayerList() for i in range(self.SIZE)]
        #print(self.hashmap)

    def size(self) -> int:
        """Return the total number of Player objects in the hash map"""
        total = 0
        for player_list in self.hashmap:
            total += len(player_list)
        return total

    def get_index(self, key : str | Player) -> int:
        """Returns an index, by hashing the key (uid | Player) and modulates it by the size of the hashmap"""
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.pearson_hash(key) % self.SIZE

    def put(self, *, key: str, name: str) -> None:
        """Adds a new Player to a PlayerList that corresponds to that index in the hash map.
        If the key already exists, updates the player's name."""
        #if key is empty
        if key == "":
            raise ValueError("Key cannot be an empty string")

        new_node = PlayerNode(Player(key, name))
        #print(f"Player uid: {new_node.player.uid}, Player name:{new_node.player.name}")

        # Use the key to calculate an index for the hash map
        index = self.get_index(key)
        #print('Index:', index)

        # Get the PlayerList at that index
        player_list = self.hashmap[index]

        #check if a player is already on that player_list (collision)
        for node in player_list:
            if node.player.uid == new_node.player.uid:
                node.player.name = name
                ##print("Player exists at Hashmap Index:", index)
                return

        # add to PlayerList // chaining
        player_list.insert_at_tail(new_node)
        #print("inserted!")

    def get(self, key : str) -> Player:
        """Retrieve a player from the PlayerList with the corresponding index in the hash map."""
        if self.size() == 0:
            raise KeyError("Hashmap is empty")

        index = self.get_index(key)
        player_list = self.hashmap[index]

        # Could add find() method in PlayerList that uses a loop
        for node in player_list:
            if node.player.uid == key:
                return node.player

        raise KeyError(f"Key '{key}' not found in hash map")

    def remove(self, key: str) -> None:
        """Remove a player from the PlayerList with the corresponding index in the hash map"""
        # use the delete_key in PlayerList
        # index = self.get_index(key)
        # player_list = self.hashmap[index]
        # player_list.delete_key(key)
        self.hashmap[self.get_index(key)].delete_key(key)

    def display(self) -> None:
        """Displays the contents of the PlayerLists in the hash map if it contains a Player"""
        for i, player_list in enumerate(self.hashmap, start=0):
            if len(player_list) > 0:
                print(f"\nPlayerList Index: {i}")
                print(f"Number of Players: {len(player_list)}")
                for node in player_list:
                    print(f"uid: {node.player.uid}, name: {node.player.name}")
                print("------------------------")