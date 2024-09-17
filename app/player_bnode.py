from __future__ import annotations
from typing import Optional
from app.player import  Player

class PlayerBNode:
    def __init__(self, player : Player) -> None:
        self._player = player
        self._left : Optional[PlayerBNode] = None
        self._right : Optional[PlayerBNode] = None

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, player: Player) -> None:
        self._player = player

    @property
    def left(self) -> Optional[PlayerBNode]:
        return self._left

    @left.setter
    def left(self, node: Optional[PlayerBNode]) -> None:
        self._left = node

    @property
    def right(self) -> Optional[PlayerBNode]:
        return self._right

    @right.setter
    def right(self, node: Optional[PlayerBNode]) -> None:
        self._right = node

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.player})'

    def __lt__(self, other: 'PlayerBNode') -> bool:
        if hasattr(other, 'player'):
            return self.player.player_name < other.player.player_name

    def __eq__(self, other):
        if hasattr(other, 'player'):
            return self.player.player_name == other.player.player_name

    def __gt__(self, other: 'PlayerBNode') -> bool:
        if hasattr(other, 'player'):
            return self.player.player_name > other.player.player_name