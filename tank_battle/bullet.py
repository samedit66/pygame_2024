from direction import Direction
from cell_pos import CellPos
from field import Field
from game_object import GameObject

class Bullet(GameObject):
    MAX_DISTANCE = 3

    def __init__(self, direction: Direction):
        self._direction = direction
        self._position = None
        self._field = None
        self._is_alive = True
        self._way_distance = 0
        self._texture = None

    def render(self):
        pass

    def set_field(self, field):
        self._field = field

    def set_position(self, position):
        self._position = position

    def is_alive(self):
        return self._is_alive
    
    def get_position(self):
        return self._position
    
    def die(self):
        self._is_alive = False

    def move(self):
        if not self.is_alive():
            return
        
        elif self._way_distance == Bullet.MAX_DISTANCE:
            self.die()
            return

        neighbor = self._position.get_neighbour(self._direction)
        if neighbor is None:
            self.die()
            return
        elif self._field.is_occupied(neighbor):
            unit_at_position = self._field.get_unit(neighbor)

            if isinstance(unit_at_position, Tank):
                unit_at_position.die()
                self.die()
            elif isinstance(unit_at_position, Wall):
                self.die()
        else:
            self._way_distance += 1
            self._position = neighbor

