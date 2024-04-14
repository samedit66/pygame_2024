from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    @staticmethod
    def valoues():
        return[Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]