from texture import TitleTexture
from Settings import Settings


class GameObjectt():

    def __init__(self, texture_file, title_pos, angle=None, position=None):
        self.texture = TitleTexture(texture_file, Settings.CELL_SIZE)
        self.title_pos = title_pos
        self .angle = angle
        self.position = position

    def set_position(self, new_position):
        self.position = new_position

    def render(self):
        return self.texture.get(self.title_pos, self_pos)