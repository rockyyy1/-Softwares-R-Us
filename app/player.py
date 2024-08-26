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
        """Constructs a Player object

        Parameters
        id : str
            A unique identifier id
        player_name : str
            The player's name
        """
        self._uid = uid
        self.player_name = player_name

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

    def __str__(self):
        """Returns the player's id and name"""
        return f"Player id: {self.uid}\nPlayer name: {self.name}"

    def __hash__(self):
        """Returns the hash of the player's uid using the Pearson hash class method"""
        return self.pearson_hash(self.uid)

    def __eq__(self, other):
        """Returns true if two players are equal, otherwise false"""
        return self.uid == other.uid

    @classmethod
    def pearson_hash(cls, key : str) -> int:
        """Returns the hashed value of the player's uid"""
        hash_ = 0
        for char in key:
            hash_ = pearson_table[hash_ ^ ord(char)]
        return hash_

