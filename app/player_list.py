from __future__ import annotations

from app.player_node import PlayerNode
from typing import Generator


class PlayerList:
    """A class representing a doubly linked list of PlayerNodes.

        Attributes:
            _head (PlayerNode): The head node of the list.
            _tail (PlayerNode): The tail node of the list.

    Note: Docstrings were generated with the help of AI, but edited to fit Google Style https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html#example-google
    """
    def __init__(self, _head: PlayerNode | None = None, _tail : PlayerNode | None = None) -> None:
        """Constructs a PlayerList object.

        Parameters
        head (PlayerNode or None) : The head node of the list (default is None).
        tail (PlayerNode or None) : The end node of the list (default is None).
        """
        self._head = _head
        self._tail = _tail

    @property
    def is_empty(self) -> bool:
        """Returns true if list is empty"""
        return self._head is None

    @property
    def head(self) -> PlayerNode | None:
        """Returns the head node of the list"""
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
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

    def delete_from_head(self) -> None:
        """Delete a player from the head of the list."""
        if self.is_empty:
            raise IndexError("List is empty")
        #single item in list
        elif self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.previous = None

    def delete_from_tail(self) -> None:
        """Delete a player from the tail of the list."""
        if self.is_empty:
            raise IndexError("List is empty")
        elif self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.previous
            self._tail.next = None

# trying this Generator thing out:
# Resource: https://github.com/NM-TAFE/diploma-adv-prog-python/blob/2024/s2/raf/joo/simple-linked-list/src/linked_list.py
    def __iter__(self) -> Generator[PlayerNode, None, None]:
        """iteration over the nodes in the linked list using a for loop"""
        node = self._head
        while node is not None:
            yield node
            node = node.next

    def delete_key(self, key : str) -> None:
        """Delete a player node from the list with a given key"""
        if self.is_empty:
            raise IndexError("List is empty")

        for node in self:
            # Used AI to help me understand better, code comments are my own
            if node.key == key:
                print("Key found")
                # if the node has a previous node, make that node's NEXT node the removed one's next
                if node.previous:
                    node.previous.next = node.next

                # if the node is at the head, make the next node the head
                else:
                    self._head = node.next

                # if the node has a next node, make the node's previous the removed one's previous
                if node.next:
                    node.next.previous = node.previous

                # if the node is at the tail, make the previous the tail
                else:
                    self._tail = node.previous
                return

        print("Key not found")
        raise KeyError(f"Key: {key} not found")

#Refactor display such that you do need to repeat basically the same pattern for forward and backward
    def display(self, forward : bool = True) -> str:
        """Iterates over linked list and prints each node

        Parameters
        forward : bool
            True prints list head to tail
            False prints list tail to head"""
        display_output = ""
        if self.is_empty:
            display_output += "List is empty"
        else:
            # if forward:
            #     display_output += "Head -> Tail\n"
            #     current_node = self._head
            #     node_to_get = "next"
            # else:
            #     display_output += "Tail -> Head\n"
            #     current_node = self._tail
            #     node_to_get = "previous"

            #My code above - Used AI to help learn  make it more pythonic
            display_output += "Head -> Tail\n" if forward else "Tail -> Head\n"
            current_node = self._head if forward else self._tail
            node_to_get = "next" if forward else "previous"

            while current_node:
                display_output += getattr(current_node.player, "player_name")
                #check if the next 'node to get' (either next or previous) exists - to print an arrow
                if getattr(current_node, node_to_get):
                    display_output += " -> "
                #set the next node to get (next or previous)
                current_node = getattr(current_node, node_to_get)

        print(display_output)
        return display_output



