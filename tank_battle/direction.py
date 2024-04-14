from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    @staticmethod
    def values():
        return [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
    