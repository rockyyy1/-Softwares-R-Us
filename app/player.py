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

    def __str__(self):
        """Returns the player's id and name"""
        return f"Player id: {self.uid}\nPlayer name: {self.name}"
