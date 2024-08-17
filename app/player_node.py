from __future__ import annotations

from app.player import Player

# Resources used for setter/getters:
# https://github.com/NM-TAFE/diploma-adv-prog-python/blob/2024/s2/raf/joo/simple-linked-list/src/node.py

class PlayerNode:
    """
    A class to represent a node in a doubly linked list which stores player objects

    Attributes
        player (Player) : The player object associated with this node.
        previous (PlayerNode or None) : The previous node in the linked list.
        next (PlayerNode or None) : The next node in the linked list.
        key (str) : The string representation of the uid of the player object.
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
    def next(self) -> PlayerNode | None:
        """Returns the next node in the linked list"""
        return self._next

    @next.setter
    def next(self, node : PlayerNode | None) -> None:
        """Sets the next node in the linked list"""
        if not isinstance(node, (PlayerNode, type(None))):
            raise TypeError("Next must be a Node instance or None.")
        self._next = node

    @property
    def previous(self) -> PlayerNode | None:
        """Returns the previous node in the linked list"""
        return self._previous

    @previous.setter
    def previous(self, node : PlayerNode | None) -> None:
        """Sets the previous node in the linked list"""
        if not isinstance(node, (PlayerNode, type(None))):
            raise TypeError("Previous must be a Node instance or None.")
        self._previous = node

    @property
    def key(self) -> str:
        """Returns the string representation of the uid of the player object"""
        return self._player.uid

    def __str__(self) -> str:
        """string representing the node object"""
        return f"Node: {self._player}"