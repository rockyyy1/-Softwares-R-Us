from __future__ import annotations

import random

random.seed(42)

pearson_table = [random.randint(0, 255) for _ in range(256)]

class Player:
    """A class to represent a player

    Attributes
    id : str
        A unique identifier id
    player_name : str
        The player's name
    """

    def __init__(self, uid: str, player_name: str) -> None:
        self._uid = uid
        self.player_name = player_name
        self._score = 0

    @property
    def uid(self):
        """Returns the unique identifier id"""
        return self._uid

    @property
    def name(self):
        """Returns the player's name"""
        return self.player_name

    @name.setter
    def name(self, value):
        self.player_name = value

    @property
    def score(self) -> int:
        """Returns the player's score"""
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        """Setter for player's score"""
        if value < 0:
            raise ValueError("Score must be positive")
        if not isinstance(value, int):
            raise TypeError("Type must be integer")
        self._score = value

    def __str__(self):
        """Returns the player's id and name"""
        return f"Player id: {self.uid}\nPlayer name: {self.name}"

    def __hash__(self):
        """Returns the hash of the player's uid using the Pearson hash class method"""
        return self.pearson_hash(self.uid)

    # def __eq__(self, other):
    #     """Returns true if two players are equal, otherwise false"""
    #     return self.uid == other.uid

    # ==
    def __eq__(self, other : Player | int) -> bool:
        """Compares two players based on their scores"""
        if not isinstance(other, (Player, int)):
            # raise NotImplemented
            return False
        if isinstance(other, int):
            return self.score == other
        return self.score == other.score

    # <
    def __lt__(self, other : Player | int) -> bool:
        """Compares this player's score is less than another player's score"""
        if not isinstance(other, (Player, int)):
            raise TypeError("Cannot compare.")
        if isinstance(other, int):
            return self.score < other
        return self.score < other.score

    # <=
    def __le__(self, other : Player | int) -> bool:
        """Compares this player's score is less than or equal to other player's score"""
        if not isinstance(other, (Player, int)):
            raise TypeError("Cannot compare.")
        if isinstance(other, int):
            return self.score <= other
        return self.score <= other.score

    # >
    def __gt__(self, other : Player | int) -> bool:
        """Compares this player's score is greater than other player's score"""
        if not isinstance(other, (Player, int)):
            raise TypeError("Cannot compare.")
        if isinstance(other, int):
            return self.score > other
        return self.score > other.score

    # >=
    def __ge__(self, other : Player | int) -> bool:
        """Compares this player's score is greater than or equal to other player's score"""
        if not isinstance(other, (Player, int)):
            raise TypeError("Cannot compare.")
        if isinstance(other, int):
            return self.score >= other
        return self.score >= other.score

    # !=
    def __ne__(self, other : Player | int) -> bool:
        """Compares this player's score is not equal to other player's score"""
        if not isinstance(other, (Player, int)):
            # raise TypeError("Cannot compare. Not same type")
            return True
        if isinstance(other, int):
            return self.score != other
        return self.score != other.score

    @classmethod
    def pearson_hash(cls, key : str) -> int:
        """Returns the hashed value of the player's uid"""
        hash_ = 0
        for char in key:
            hash_ = pearson_table[hash_ ^ ord(char)]
        return hash_

    @staticmethod
    def sort_players_by_score(players_list : list) -> list:
        """Sorts the players by their score in descending order using Quicksort"""
        # create a copy so original remains the same
        players_list_copy = players_list[:]

        # if length of array is 1, just return it
        length = len(players_list_copy)
        if length <= 1:
            return players_list_copy
        else:
            #pivot is the last item in list -- remove at same time
            pivot = players_list_copy.pop()

        items_greater_than_pivot = []
        items_lower_than_pivot = []

        for item in players_list_copy:
            # < operator for descending | > for ascending
            if item < pivot:
                items_greater_than_pivot.append(item)
            else:
                items_lower_than_pivot.append(item)

        #call itself - recursive function
        return Player.sort_players_by_score(players_list = items_lower_than_pivot) + [pivot] + Player.sort_players_by_score(players_list = items_greater_than_pivot)
