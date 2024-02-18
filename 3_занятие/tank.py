import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], file_image: str):
        self.image = pygame.image.load(file_image).convert_alpha()
        self.up_image = self.image
        self.right_image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect(topleft=position)
        self.move_x = 0
        self.move_y = 0

    def process_input(self):
        self.move_x =  self.move_y = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.move_x = -2
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.move_x = 2
            self.image = self.right_image
        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.move_y = -2
            self.image = self.up_image
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.move_y = 2

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y

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
        self.tank.process_input()

    def update_game_state(self):
        self.tank.update()

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