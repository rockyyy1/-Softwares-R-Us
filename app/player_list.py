from app.player_node import PlayerNode


class PlayerList:
    """A doubly linked list of player nodes"""

    def __init__(self, head: PlayerNode = None, tail : PlayerNode = None) -> None:
        """Constructs a PlayerList object.

        Parameters
        head : PlayerNode or None
            The head node of the list (default is None).
        tail : PlayerNode or None
            The end node of the list (default is None).
        """
        self._head = head
        self._tail = tail

    @property
    def is_empty(self) -> bool:
        """Returns true if list is empty"""
        return self._head is None

    @property
    def head(self) -> PlayerNode:
        """Returns the head node of the list"""
        return self._head

    @property
    def tail(self) -> PlayerNode:
        """Returns the tail node of the list"""
        return self._tail

    def insert_at_head(self, new_node: PlayerNode) -> None:
        """Insert a player at the head of the list."""
        if self.is_empty:
            self._head = new_node
            self._tail = new_node
            #print("List was empty")
        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node
            #print("List was not empty")

    def insert_at_tail(self, new_node: PlayerNode) -> None:
        """Insert a player at the tail of the list."""
        if self.is_empty:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail.next = new_node
            new_node.previous = self._tail
            self._tail = new_node

