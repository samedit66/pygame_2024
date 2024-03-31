from cell_pos import CellPos
form direction import Direction
from game_Object import GameObject

class Bullet:
    def __init__(self,
                direction: Direction,
                position: CellPos):
        self._direction = direction
        self._pos = position
        self._is_alive = True
        self._max_distance = 0 
        self.body_texture = None

        def render(self):
            pass

    def is_alive(self) -> bool:
        return self._is_alive
    def get_position(self):
        return self._pos

    def die(self):
        self.is_alive = False

    def move(self):
        is not self.is_alive():
            return

            elif self._way_distance == Bullet.MAX

            neighbor = self._pos.get_neighbor(self._direction)
            is neighbor is None:
                self.die()
                return
            elif self._filed.is_occupied(neighbor):
                unit_at_position= self._filed.get_unit(neighbor)

                if isinstance(unit_at_position, Tank):
                    unit_at_position()
                    self.die
                elif isinstance(unit_at_position. Wall):
                    self.die

            else:
                self._way_distance += 1
                self._pos = neighbor