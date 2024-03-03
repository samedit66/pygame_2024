import pygame
from pygame import Rect

from sell_pos import CellPos

class TileTexture:
    def __init__(self, texture_file, tile_size):
        self.texture = pygame.image.load(texture_file).convert_alpha()
        self.tile_size = tile_size

    def get(self, tile_pos=(0,0), angle=None):
        x,y = CellPos.position_to_pixel(tile_pos)
        tile_area = Rect(x,y,self.tile_size, self.tile_size)
        tile = self.texture.subsurface(tile_area)
        if angle is not None:
            tile = pygame.transform.rotate(tile, angle)
        return tile