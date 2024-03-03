import pygame
from pygame import rect

from cell_pos import CellPos

class TitleTexture:
    def __init__(self, texture_file: str, title_size: int):
        self.texture = pygame.image.load(texture_file).convert_alpha()
        self.title_size = title_size

    def get(self, tile_pos=(0, 0), angle=None):
    x, y = cell_pos.position_to_pixel(title_pos)
    tile_area = Rect(x, y, self.tile_size, self.tile_size)
    tile = self.texture.subsurface(tile_area)
    if angle is not None:
        tile = pygame.transform.rotate(tile, angle)
    return tile
