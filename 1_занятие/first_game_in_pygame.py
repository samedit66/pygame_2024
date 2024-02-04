import pygame # Импортируем библиотеку


pygame.init() # Включаем пайгейм

# Создаем окно будущей игры с заданным размерами в пикселях
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
MAIN_WINDOW_COLOR = (255, 255, 255) # Это белый в RGB

main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Моя первая игра")

# Задаем начальные параметры для прямоугольника
left_top_x, left_top_y, width, height = 0, 0, 200, 300
rectangle = pygame.Rect(left_top_x, left_top_y, width,  height)
color = (255, 0, 0) # Цвета задаются в RGB, это красный

running = True
while running:
    # "Ввод данных" от пользователя
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Красим фон главного окна в белый цвет
    main_window.fill(MAIN_WINDOW_COLOR)

    # Рисуем прямоугольник
    pygame.draw.rect(main_window, color=color, rect=rectangle)
    pygame.display.update()
    
pygame.quit()