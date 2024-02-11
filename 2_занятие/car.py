import pygame


class Game():

    def __init__(self):
        pygame.init()

        # Ширина и высота игрового окна
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 800
        
        # Ограничиваемся 60 кадрами в секунду
        self.FPS = 60

        # Создаем главное игровое окно
        self.main_window = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        )

        # "Часы" ограничивают количество FPS в секунду
        self.clock = pygame.time.Clock()

        # Статус игры
        self.running = True

        # Координаты верхнего левого угла кузова (body) машины
        self.x_car = 40
        self.y_car = 400

        # Величины сдвигов по координатам при нажатии
        self.x_move = 0
        self.y_move = 0

    def process_input(self):
        self.x_move = 0
        self.y_move = 0

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.x_move += 8
                elif event.key == pygame.K_LEFT:
                    self.x_move -= 8

    def update_game_state(self):
        self.x_car += self.x_move
        self.y_car += self.y_move

    def draw_car(self, x_body_start, y_body_start):
        # Отрисовка кузова
        body_width = 240
        body_height = 100
        x_body = x_body_start
        y_body = y_body_start
        body_color = pygame.color.THECOLORS["orange"]
        body = pygame.Rect(x_body, y_body, body_width, body_height)
        pygame.draw.rect(self.main_window, color=body_color, rect=body)

        # Отрисовка кабины
        cabin_width = 100
        cabin_height = 130
        x_cabin = x_body + body_width
        y_cabin = y_body - (cabin_height - body_height)
        cabin_color = pygame.color.THECOLORS["orange"]
        cabin = pygame.Rect(x_cabin, y_cabin, cabin_width, cabin_height)
        pygame.draw.rect(self.main_window, color=cabin_color, rect=cabin)

        # Отрисовка окна в кабине
        window_width = 60
        window_height = 50
        x_offset_cabin = 20
        y_offset_cabin = 10
        x_window = x_cabin + x_offset_cabin
        y_window = y_cabin + y_offset_cabin
        window_color = pygame.color.THECOLORS["skyblue"]
        window = pygame.Rect(x_window, y_window, window_width, window_height)
        pygame.draw.rect(self.main_window, color=window_color, rect=window)

        # Отрисовка контура окна
        window_contour_color = pygame.color.THECOLORS["black"]
        window_contour_width = 2
        pygame.draw.rect(self.main_window,
                         color=window_contour_color,
                         rect=window,
                         width=window_contour_width)


        wheel_center_color = pygame.color.THECOLORS["black"]
        wheel_center_radius = 5

        # Отрисовка колеса у кузова
        left_wheel_radius = 25
        x_offset_body = 40
        y_offset_body = 90
        x_left_wheel = x_body + x_offset_body
        y_left_wheel = y_body + y_offset_body
        left_wheel_color = pygame.color.THECOLORS["grey"]
        pygame.draw.circle(
            self.main_window,
            color=left_wheel_color,
            center=(x_left_wheel, y_left_wheel),
            radius=left_wheel_radius
        )
        pygame.draw.circle(
            self.main_window,
            color=wheel_center_color,
            center=(x_left_wheel, y_left_wheel),
            radius=wheel_center_radius
        )

        # Отрисовка колеса у кабины
        right_wheel_radius = 25
        x_offset_cabin = 60
        y_offset_cabin = 120
        x_right_wheel = x_cabin + x_offset_cabin
        y_right_wheel = y_cabin + y_offset_cabin
        right_wheel_color = pygame.color.THECOLORS["grey"]
        pygame.draw.circle(
            self.main_window,
            color=right_wheel_color,
            center=(x_right_wheel, y_right_wheel),
            radius=right_wheel_radius
        )
        pygame.draw.circle(
            self.main_window,
            color=wheel_center_color,
            center=(x_right_wheel, y_right_wheel),
            radius=wheel_center_radius
        )

    def render(self):
        main_window_color = pygame.color.THECOLORS["white"]
        self.main_window.fill(main_window_color)

        self.draw_car(self.x_car, self.y_car)

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