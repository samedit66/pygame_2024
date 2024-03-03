import pygame

from direction import Direction
from texture import TitleTexture
from Settings import Settings

class Tank():

    def __init__(self):
        self.filed = None
        self.position = None
        self.body_texture_file = 'thanks_images/blue/body.png'
        self.turret_texture_gile = "thanks_immages/blue/turret2.png"
        self.body_texture = TitleTexture(self.body_texture_file, Settings.CELL_SIZE)
        self.body_image = self_body_texure.get()
        self.turret_texture = TitleTexture(self.turret_texture_gile, Settings.CELL_SIZE
        self.turret_image= self.turret_texture.get()