from __future__ import annotations

import random

MAX_SCORE = 5000
ids = list(range(10000))


class Player:
    def __init__(self):
        self.id = ids.pop(0)
        self.score = random.randint(0, MAX_SCORE)

    def __repr__(self) -> str:
        return f'player{self.id}: {self.score}'

    # Less than function
    def __lt__(self, other: Player) -> bool:
        if isinstance(other, str):
            return repr(self) < other
        if isinstance(other, int):
            return self.score < other
        if isinstance(other, Player):
            return self.score < other.score

    # Greater than
    def __gt__(self, other):
        print("Got here")

    def __eq__(self, other):
        if not isinstance(other, Player):
            raise NotImplemented
        return self.score == other.score


players = [Player() for _ in range(10)]
print("Unsorted: ", players)
# sorted(players, key=lambda x: x.score)
# print(Player() < Player())
print("Sorted: ", sorted(players))
