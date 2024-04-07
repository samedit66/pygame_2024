import pygame

from settings import Settings
from ground import *
from obstacle import Wall
<<<<<<< HEAD
from cell_pos import CellPos

class Field:
=======


class Field():
    
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495
    def __init__(self):
        self.ground = None
        self.walls = None
        self.units = []
<<<<<<< HEAD

        self._init_field()

    def can_move_to(self,position, direction):
        neighbor = position.get_neighbour(direction)
        return (neighbor is not None) and (not self.is_occupied(neighbor))
    
    def is_occupied(self, position):
        for unit in self.units:
            if unit.position == position:
                return True
        for wall in self.walls:
            if wall.position == position:
                return True
        return False

    def put_at(self, new_unit, position):
        if self.is_occupied(position):
            return False
        
        new_unit.set_field(self)
        new_unit.set_position(position)
        self.units.append(new_unit)
        return True
    def get_unit(self, position):
        for unit in self.units:
            if unit.position == position:
                return unit
            for wall in self.walls:
                if wall.position == position:
                    return wall
            return None

    def _init_field(self):
        self.ground = [
            [Grass(), Bush(), Road(), RoadCprner(), RoadCprner(-90)],
            [Bush(), Grass(), Road(), RoadCprner(90), RoadCprner(180)],
            [Grass(), Bush(), Road(), Grass(), Grass()],
            [Grass(), Grass(), Road(), RoadCprner(), RoadCprner(-90)],
            [Grass(), Grass(), Road(), RoadCprner(90), RoadCprner(180)],
=======
        self.bullets = []

        self._init_field()

    def _init_field(self):
        self.ground = [
            [Grass(), Road(), Grass(), Grass(), Bush()],
            [Grass(), Road(), Grass(), Bush(), Grass()],
            [Road(angle=-90), TripleRoad(angle=180), Grass(), Grass(), Grass()],
            [Grass(), Road(), Grass(), Grass(), Grass()],
            [Bush(), Road(), Bush(), Grass(), Grass()],
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495
        ]

        for row in range(Settings.ROWS_COUNT):
            for col in range(Settings.COLS_COUNT):
                self.ground[row][col].set_position(CellPos(col, row))

        self.walls = [
<<<<<<< HEAD
            Wall(position= CellPos(0,3)), Wall(position= CellPos(1,3), angle= 180)
        ]

=======
            Wall(position=CellPos(0, 3)), Wall(position=CellPos(1, 3), angle=180)
        ]
        
    def _is_occupied(self, pos):
        for unit in self.units:
            if unit.position == pos:
                return True
        for wall in self.walls:
            if wall.position == pos:
                return True
        return False

    def put_at(self, new_unit, pos):
        if self._is_occupied(pos):
            return False
            
        new_unit.set_field(self)
        new_unit.set_position(pos)
        self.units.append(new_unit)
        return True

    def add_bullet(self, bullet):
        bullet.set_field(self)
        self.bullets.append(bullet)

    def can_move_to(self, position, direction):
        neighbor = position.get_neighbor(direction)
        return (neighbor is not None) and (not self._is_occupied(neighbor))
    
>>>>>>> 93e7d934b788d6586b9b9ccdf853a02bd94ae495
    def render_ground(self, field):
        for i in range(len(self.ground)):
            for j in range(len(self.ground[i])):
                ground_obj = self.ground[i][j]
                ground_pixel_pos = CellPos.position_to_pixel(ground_obj.position)
                field.blit(ground_obj.render(), ground_pixel_pos)

    def render_walls(self, field):
        for wall in self.walls:
            wall_pixel_pos = CellPos.position_to_pixel(wall.position)
            field.blit(wall.render(), wall_pixel_pos)

    def render_units(self, field):
        for unit in self.units:
            unit_pixel_pos = CellPos.position_to_pixel(unit.position)
            field.blit(unit.render(), unit_pixel_pos)

    def render(self):
        field = pygame.Surface((Settings.PIXEL_WIDTH, Settings.PIXEL_HEIGHT))

        self.render_ground(field)
        self.render_walls(field)
        self.render_units(field)

        return field