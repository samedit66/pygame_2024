from random import randint


def initialize():
    """
    Задает начальные настройки игры "Угадай число"
    """
    LOW_BOUND = 1
    HIGH_BOUND = 100
    guessed_number = randint(LOW_BOUND, HIGH_BOUND)
    return LOW_BOUND, HIGH_BOUND, guessed_number


def process_input():
    """
    Обрабатывает ввод данных от пользователя
    """
    valid_input = False

    while not valid_input:
        user_input = input("Какое число я загадал? ")
        if not user_input.isdigit():
            print("Введите число!")
        else:
            valid_input = True
    
    return int(user_input)
    

def update_game_state(user_input, guessed_number):
    """
    Обновляет состояние игры
    """
    if user_input == guessed_number:
        game_state = "win"
    elif user_input < guessed_number:
        game_state = "high"
    elif user_input > guessed_number:
        game_state = "low"
    
    return game_state


def render(game_state):
    """
    Выполняет отрисовку
    """
    if game_state == "win":
        print("Молодец, правильно!")
    elif game_state == "low":
        print("Неа, я загадал число меньше")
    elif game_state == "high":
        print("Вообще не то... Мое число больше")


def is_game_over(game_state):
    """
    Проверяет завершенность игры
    """
    return game_state == "win"


def game_loop():
    """
    Выполняет главный игровой цикл
    """
    low_bound, high_bound, guessed_number = initialize()

    print(f"Я загадал число от {low_bound} до {high_bound}... {guessed_number}")

    while True:
        user_number = process_input()
        game_state = update_game_state(user_number, guessed_number)
        render(game_state)
        if is_game_over(game_state):
            break


# Запускаем игру...
game_loop()