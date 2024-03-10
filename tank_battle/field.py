import pygame

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
        return(neighbor is not None) and (not self._is_occupied(neighbor))

    def _is_occupied(self, position):
        for unit in self.units:
            if unit.position == position:
                return True
        for wall in self.walls:
            if wall.position == position:
                return True
        return False
        
    def put_at(self, new_unit, position):
        if self._is_occupied(position):
            return False

        new_unit.set_field(self)
        nwe_unit.set_position(position)
        self.units.append(new_unit)
        return True

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

    def _init_field(self):
        self.ground = [
            [Grass(), Road(), Grass(), Grass(), Bush()],
            [Grass(), Road(), Grass(), Bush(), Grass()],
            [Road(angle=-90), TripleRoad(angle=180), Grass(), Grass(), Grass(),],
            [Grass(), Road(), Grass(), Grass(), Grass()],
            [Bush(), Road(), Bush(), Grass(), Grass()],
        ]

    for row in range(Settings.ROWS_COUNT):
        for col in range(Settings.COLS_COUNT):
            self.ground[row][col].set_position(CellPos(col,row))

    self.walls = [
        Wall(position=CellPos(0, 3)), Wall(position=CellPos(1, 3), angle=180)
    ]

    def render_ground(self, field):
        ...

    def render(self):
        field = pygame.Surface((Settings.PIXEL_WIDTH, Settings.PIXEL_HEIGHT))

        self.render_ground(field)

        self.render_walls(field)

        self.render_units(field)

        return field 