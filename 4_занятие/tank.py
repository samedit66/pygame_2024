import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], file_image: str):
        self.image = pygame.image.load(file_image).convert_alpha()
        self.up_image = self.image
        self.right_image = pygame.transform.rotate(self.image, -90)
        self.left_image = pygame.transform.rotate(self.image, +90)
        self.down_image = pygame.transform.rotate(self.image, -180)

        self.weapon = pygame.image.load('tanks_images/desert/turret2.png').convert_alpha()
        self.weapon = self.weapon.subsurface(pygame.Rect(0,0,128,128))

        self.up_weapon = self.weapon
        self.left_weapon = pygame.transform.rotate(self.weapon, 90)
        self.right_weapon = pygame.transform.rotate(self.weapon, -90)
        self.down_weapon = pygame.transform.rotate(self.weapon, 180)


        self.rect = self.image.get_rect(topleft=position)
        self.weapon_rect = self.weapon.get_rect(topleft= position)
        self.move_x = 0
        self.move_y = 0


    def process_input(self):
        self.move_x = self.move_y = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.move_x = -5
            self.image = self.left_image
            self.weapon = self.left_weapon
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.move_x = 5   
            self.image = self.right_image
            self.weapon = self.right_weapon
        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.move_y = -5
            self.image = self.up_image
            self.weapon = self.up_weapon
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.move_y = 5
            self.image = self.down_image
            self.weapon = self.down_weapon


    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.weapon_rect.x += self.move_x
        self.weapon_rect.y += self.move_y

    def render(self, window):
        window.blit(self.image, self.rect)
        window.blit(self.weapon, self.weapon_rect)





class Game:
    
    def __init__(self):
        pygame.init()

        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 600
        self.FPS = 60

        self.main_window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tank = Tank(position = (0,0), file_image= 'tanks_images/red/body.png')
    
    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
        self.tank.process_input()


    def update_game_state(self):
        self.tank.update()

    def render(self):
        self.main_window.fill(pygame.color.THECOLORS['white'])

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