from texture import TileTexture
from settings import Setiings

class GameObject():
    def __init__(self, texture_file, tile_pos, angle = None, position= None):
        self.texture = TileTexture(texture_file, Settings.CELL_SIZE)
        self.tile_pos = tile_pos
        self.angle = angle 
        self.position = position 

    def set_position(self, new_position):
        self.position = new_position

    def render(self):
        return self.texture.get(self.tile_pos, self.angle)