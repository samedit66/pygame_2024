import Pygame 

from settings import Settings 
from ground import * 
from obstacle import Wall 

class Field():
    def __init__(self):
        self.ground = None 
        self.walls = None 
        self.units = []

        self._init_field() 

    def can_move_to(self, position, direction):
        neighbor = position.get_neighbor(direction)
        return (neighbor is not None) and (not self._is_occupied(neighbor))
    
    def _is_occupied(self, position):
        for unit in self.units:
            if unit.position == position:
                return True
        for wall in self.walls:
            if wall.position == position:
                return True
        return False 