import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, image_file, position):
        pygame.sprite.Sprite.__init__(self)
        # Загружаем исходную картинку, танк "смотрит" вверх.
        # Не забываем в конце вызывать функцию convert_alpha(), чтобы ускорить
        # загрузку картинки танка в дальнейшем.
        self.image = pygame.image.load(image_file).convert_alpha()
        # Картинка для танка, когда он направлен вверх
        self.up_image = self.image
        # Картинка для танка, когда он направлен влево
        self.left_image = pygame.transform.rotate(self.image, 90)
        # А остальные картинки делаете сами...
        self.rect = self.image.get_rect(topleft=position)
        # Хранят сдвиги в пикселях, насколько танк перемещается при нажатии клавиш
        self.move_x = 0
        self.move_y = 0

    def process_input(self):
        self.move_x = 0
        self.move_y = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.move_x = -2
            self.image = self.left_image
        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.move_y = -2
            self.image = self.up_image
        # Код для обработки движения ВПРАВО и ВНИЗ самостоятельно!!!

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def render(self, screen):
        screen.blit(self.image, self.rect)


class Game():
    
    def __init__(self):
        pygame.init()

        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 800
        self.FPS = 60

        self.main_window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tank = Tank("tanks_images/blue_tank.png", (0, 0))

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