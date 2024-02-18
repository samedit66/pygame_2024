
import pygame



class Tank(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], file_image: str):
        self.image = pygame.image.load(file_image).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

    def update(self):
        pass

    def render(self, window):
        window.blit(self.image, self.rect)


class Game:
    
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 600
        self.FPS = 60   
        self.main_window = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
            )

        self.clock = pygame.time.Clock()
        self.running = True
        self.tank = Tank(position=(0, 0), file_image="tanks_images/blue_tank.png")


    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

    def update_game_state(self):
        pass

    def render(self):
        self.main_window.fill(pygame.color.THECOLORS["white"])

        self.tank.render(self.main_window)
        pygame.display.update()

    def game_loop(self):
        while self.running:
            self.process_input()
            self.update_game_state()
            self.render()
            self.clock.tick(self.FPS)
        pygame.quit()