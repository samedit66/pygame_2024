import pygame # Импортируем библиотеку

pygame.init()

class Game():

    def __init__(self):

        # Ширина и высота игрового окна
        self.WINDOW_WIDTH = 1000
        self.WINDOW_HEIGHT = 1000
        
        # Ограничиваемся 60 кадрами в секунду
        self.FPS = 60

        # Создаем главное игровое окно
        self.main_window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # "Часы" ограничивают количество FPS в секунду
        self.clock = pygame.time.Clock()

        # Статус игры
        self.running = True

        # Координаты верхнего левого угла кузова (body) машины
        self.x = 200
        self.y = 200

        # Величины сдвигов по координатам при нажатии
        self.x_move = 0
        self.y_move = 0

    def process_input(self):
        self.move_x =  self.move_y = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.move_x = -10
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.move_x = 10
        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.move_y = -100
            pygame.time.wait(1000)

    def update_game_state(self):
        self.x += self.x_move
        self.y += self.y_move

    def draw(self):
        x, y, width, height = 0, 0, 200, 300
        rectangle = pygame.Rect(x, y, width - 100,  height- 100)
        color = (99, 99, 99)
        pygame.draw.rect(self.main_window, color=color, rect=rectangle)


    def render(self):
        main_window_color = pygame.color.THECOLORS["white"]
        self.main_window.fill(main_window_color)
        self.draw()

        # Не забываем обновить экран, как только что-то нарисовали,
        # иначе ничего не появится
        pygame.display.update()

    def main_loop(self):
        while self.running:
            self.process_input()
            self.update_game_state()
            self.render()
            self.clock.tick(self.FPS)

        pygame.quit()


game = Game()
game.main_loop()