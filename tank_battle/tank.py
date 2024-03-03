import pygame

from direction import Direction
from texture import TileTexture
from settings import Settings


class Tank():

    def __init__(self):
        self.field = None
        self.position = None
        self.body_texture_file = 'tanks_images/desert/body.png'
        self.turret_texture_file = 'tanks_images/camo/turret2.png'
        self.body_texture = TileTexture(self.body_texture_file, Settings.CELL_SIZE)
        self.body_image = self.body_texture.get()
        self.turret_texture = TileTexture(self.turret_texture_file, Settings.CELL_SIZE)
        self.turret.image = self.turret_texture.get()