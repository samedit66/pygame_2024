import pygame 

from settings import Settings 
from ground import * 
from obstacle import WallMiddle
from obstacle import WallEnd
from obstacle import WallCorner
from obstacle import Tower
from bullet import Bullet 

class Field():
    def __init__(self):
        self.ground = None 
        self.walls = None 
        self.units = []

        self._init_field() 

    def clear_dead_units(self):
        self.units = [unit for unit in self.units if unit.is_alive()]

    def get_bullets(self):
        return [unit for unit in self.units if isinstance(unit, Bullet)]

    def can_move_to(self, position, direction):
        neighbor = position.get_neighbor(direction)
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

    def render(self):
        field = pygame.Surface((Settings.PIXEL_WIDTH, Settings.PIXEL_HEIGHT))

        self.render_ground(field)
        self.render_walls(field)
        self.render_units(field)

        return field
    
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
            [Grass(), Road(), Grass(), Grass(), Grass()],
            [Grass(), Road(), Grass(), Bush(), Grass()],
            [Road(angle = 90), QuadRoad(), Road(angle = 90), Road(angle = 90), TripleRoad(angle = -90),],
            [Grass(), Road(), Grass(), Crater(), Road()],
            [Bush(), Road(), Grass(), Grass(), Road()],
        ]

        for row in range(Settings.ROWS_COUNT):
            for col in range(Settings.COLS_COUNT):
                self.ground[row][col].set_position(CellPos(col, row))

        self.walls = [
            WallCorner(position = CellPos(2, 0), angle=90), 
            WallMiddle(position = CellPos(3, 0)),
            WallMiddle(position = CellPos(4, 0)),
            WallCorner(position = CellPos(2, 4), angle=180),
            WallCorner(position = CellPos(3, 4)),
            Tower(position = CellPos(2, 1), angle = 90),
            Tower(position = CellPos(2, 3), angle = -90)
        ]
