from direction import Direction
from cell_pos import CellPos
from game_object import GameObject

class Bullet(GameObject):
    #пуля летит максимум 3 клетки
    MAX_DISTANCE = 3

    def __init__(self, direction: Direction):
        self._direction = direction
        self._pos = None
        self._is_alive = True
        self._way_distance = 0
        self._field = None
        self._texture = None

    def render(self):
        pass 

    def set_field(self, field):
        self._field = field

    def set_position(self, position):
        self._pos = position

    def is_alive(self) -> bool:
        return self._is_alive

    def get_position(self):
        return self._pos

    def die(self):
        self._is_alive = False

    def move(self):
        if not self.is_alive():
            return
        if self._way_distance == Bullet.MAX_DISTANCE:
            self.die()
            return

        neighbor = self._pos.get_neighbor(self._direction)
        if neighbor is None:
            self.die()
            return

        if set_field.is_occupied(neighbor):
            unit_at_position = self._field.get_unit(neighbor)
            if isinstance(unit_at_position,Tank):
                unit_at_position.die()
            elif isinstance(unit_at_position, Wall):
                self.die()
        else:
            self._way_distance += 1
            self._pos = neighbor
            
            