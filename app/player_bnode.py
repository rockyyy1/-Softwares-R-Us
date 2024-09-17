from __future__ import annotations
from typing import Optional
from app.player import  Player

class PlayerBNode:
    def __init__(self, player : Player) -> None:
        self._player = player
        self._left : Optional[PlayerBNode] = None
        self._right : Optional[PlayerBNode] = None

    @property
    def get_player(self) -> Player:
        return self._player

    @set_player.setter
    def set_player(self, player: Player) -> None:
        self._player = player

    @property
    def get_left(self) -> Optional[PlayerBNode]:
        return self._left

    @set_left.setter
    def set_left(self, node: Optional[PlayerBNode]) -> None:
        self._left = node

    @property
    def get_right(self) -> Optional[PlayerBNode]:
        return self._right

    @set_right.setter
    def set_right(self, node: Optional[PlayerBNode]) -> None:
        self._right = node