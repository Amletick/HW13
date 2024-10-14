import random

# Константа кармы для достижения просветления
KARMA_GOAL = 500


# Определение пользовательских исключений
class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


# Функция симуляции одного дня, возвращает случайную карму
def one_day():
    # С вероятностью 1 к 10 выбрасываем исключение
    if random.randint(1, 10) == 1:
        error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        raise error(f"Произошло исключение: {error.__name__}")

    # Возвращаем случайное количество кармы от 1 до 7
    return random.randint(1, 7)


def main():
    total_karma = 0

    # Открываем файл для записи логов
    with open("karma.log", "a") as log_file:
        # Бесконечный цикл до достижения кармы
        while total_karma < KARMA_GOAL:
            try:
                # Пытаемся получить карму за один день
                karma_today = one_day()
                total_karma += karma_today
                print(f"Получено {karma_today} кармы, всего: {total_karma}")

            except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
                # Записываем ошибку в лог-файл
                log_file.write(f"{str(e)}\n")
                print(f"Ошибка: {str(e)}")

    print("Достигнуто просветление!")


if __name__ == "__main__":
    main()
