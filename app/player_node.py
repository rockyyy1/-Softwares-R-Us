from app.player import Player


class PlayerNode:
    """A class to represent a node in a doubly linked list which stores player objects

    Attributes
    player : Player
        The player object associated with this node.
    previous : PlayerNode or None
        The previous node in the linked list.
    next : PlayerNode or None
        The next node in the linked list.
    key : str
        The string representation of the uid of the player object.

    Methods
    __str__():
        Returns a string representation of the node.
    """

    def __init__(self, player: Player):
        """Constructs the player node"""
        self._player = player
        self._previous = None
        self._next = None

    @property
    def player(self):
        """Returns the player object associated with this node"""
        return self._player

    @property
    def next(self):
        """Returns the next node in the linked list"""
        return self._next

    @next.setter
    def next(self, next_node):
        """Sets the next node in the linked list"""
        self._next = next_node

    @property
    def previous(self):
        """Returns the previous node in the linked list"""
        return self._previous

    @previous.setter
    def previous(self, previous_node):
        """Sets the previous node in the linked list"""
        self._previous = previous_node

    @property
    def key(self):
        """Returns the string representation of the uid of the player object"""
        return self._player.uid

    def __str__(self):
        """string representing the node object"""
        return f"Node: {self._player}"