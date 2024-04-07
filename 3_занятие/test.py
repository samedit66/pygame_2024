import pygame


class Tank(pygame.sprite.Sprite):

    def __init__(self, image_file, position):
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
    
    def render(self, window):
        window.blit(self.image, self.rect)


class Game():

    def __init__(self):
        pygame.init()

        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 800
        self.FPS = 60

        self.main_window = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        )
        self.clock = pygame.time.Clock()
        self.running = True
        self.tank = Tank("tanks_images/blue_tank.png", (0, 0))

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


game = Game()
game.game_loop()