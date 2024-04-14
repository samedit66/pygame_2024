from cell_pos import CellPos
from direction import Direction
from game_object import GameObject
from traits import IsAlive, SelfMoving

class Bullet(GameObject, IsAlive):
    MAX_DISTANCE = 3

    def __init__(self,
                direction: Direction):
        GameObject.__init__(self, "tanks_images/bullet.png", (0, 0))
        IsAlive.__init__(self)
        SelfMoving.__init__(self)
        self._direction = direction
        self._way_distance = 1
        self.body_texture = None
        self._field = None

    def set_field(self, new_field):
        self._field = new_field

    def move(self):
        if not self.is_alive():
            return
        elif self._way_distance == Bullet.MAX_DISTANCE:
            self.die()
            return

        neighbor = self.position.get_neighbor(self._direction)
        if neighbor is None:
            self.die()
            return
            
        elif self._field.is_occupied(neighbor):
            unit_at_position = self._field.get_unit(neighbor)

            if isinstance(unit_at_position, IsAlive):
                unit_at_position.die()
            self.die()
        else:
            self._way_distance += 1
            self.position = neighbor