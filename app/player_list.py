from app.player_node import PlayerNode


class PlayerList:
    """A doubly linked list"""

    def __init__(self, head = None) -> None:
        """Constructs a PlayerList object.

        Parameters
        head : PlayerNode or None, optional
            The initial head of the list (default is None).
        """
        self._head = head

    @property
    def is_empty(self) -> bool:
        """Returns true if list is empty"""
        return self._head is None

    def insert_at_head(self, new_node: PlayerNode) -> None:
        """Insert a player at the head of the list."""
        if self.is_empty:
            self._head = new_node
            #print("List was empty")
        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node
            #print("List was not empty")

