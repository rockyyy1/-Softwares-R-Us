from __future__ import annotations

from player import Player
from player_list import PlayerList

class PlayerHashMap:
    def __init__(self):
        self.size = 10
        self.hash_map = [PlayerList() for i in range(self.size)]
        print(self.hash_map)

    def get_index(self, key : str | Player) -> str:
        if is_instance(key, Player):
            return hash(key) % self.size
        else:
            return Player.hash(key) % self.size

    def __setitem__(self, key: str, name : str) -> None:

test = PlayerHashMap()
