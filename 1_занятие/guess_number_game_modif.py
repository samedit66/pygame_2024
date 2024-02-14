from random import randint


def initialize():
    """
    Задает начальные настройки игры "Угадай число"
    """
    LOW_BOUND = 1
    HIGH_BOUND = 100
    guessed_number = randint(LOW_BOUND, HIGH_BOUND)
    tries = 5
    return LOW_BOUND, HIGH_BOUND, guessed_number, tries


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
    

def update_game_state(user_input, guessed_number, tries):
    """
    Обновляет состояние игры
    """

    assert tries >= 1

    if user_input != guessed_number and tries == 1:
        game_state = "lose"
    elif user_input > guessed_number:
        game_state = "low"
    elif user_input < guessed_number:
        game_state = "high"
    else:
        game_state = "win"

    return game_state, tries - 1


def render(game_state, guessed_number):
    """
    Выполняет отрисовку
    """
    if game_state == "win":
        print("Молодец, правильно!")
    elif game_state == "lose":
        print(f"Извини, ты проиграл... Я загадал {guessed_number}")
    elif game_state == "low":
        print("Неа, я загадал число меньше")
    elif game_state == "high":
        print("Вообще не то... Мое число больше")


def is_game_over(game_state):
    """
    Проверяет завершенность игры
    """
    return game_state == "win" or game_state == "lose"


def game_loop():
    """
    Выполняет главный игровой цикл
    """
    low_bound, high_bound, guessed_number, tries = initialize()

    print(f"Я загадал число от {low_bound} до {high_bound}...")
    print(f"У тебя {tries} попыток, чтобы угадать!")

    while True:
        user_number = process_input()
        game_state, tries = update_game_state(user_number, guessed_number, tries)
        render(game_state, guessed_number)
        if is_game_over(game_state):
            break


# Запускаем игру...
game_loop()