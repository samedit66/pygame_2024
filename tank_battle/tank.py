import pygame

from direction import Direction
from texture import TileTexture
from settings import Settings


class Tank():
    def __init__(self):
        self.field = None
        self.position = None
        self.body_texture_file = 'tanks_image/blue/body.png'
        self.turrent_texture_file = 'tanks_image/blue/turrent2.png'
        self.body_texture = TileTexture(self.body_texture_file, Settings.CELL_SIZE)
        self.body_image = self.body_texture.get()
        self.turrent_texture = TileTexture(self.turrent_texture_file, Settings.CELL_SIZE)
        self.turrent_image = self.turrent_texture.get()
