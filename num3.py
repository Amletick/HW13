import os
import random

class LuckyNumber:
    FILE_NAME = "out_file.txt"
    TARGET_SUM = 777

    def __init__(self):
        """Инициализация программы. Удаляет старый файл при необходимости."""
        self.current_sum = 0
        self.delete_file_if_exists()

    def delete_file_if_exists(self):
        """Удаляет файл, если он существует, чтобы начать запись с чистого листа."""
        if os.path.exists(self.FILE_NAME):
            os.remove(self.FILE_NAME)

    def append_number_to_file(self, number):
        """Записывает число в файл."""
        with open(self.FILE_NAME, "a", encoding="utf-8") as file:
            file.write(f"{number}\n")

    def random_exception(self):
        """С вероятностью 1 к 13 выбрасывает исключение."""
        if random.randint(1, 13) == 1:
            raise Exception("Вас постигла неудача!")

    def run(self):
        """Основная функция программы."""
        try:
            while self.current_sum < self.TARGET_SUM:
                user_input = input("Введите число: ")

                try:
                    number = int(user_input)
                    self.random_exception()  # Проверка на случайное исключение
                    self.current_sum += number
                    self.append_number_to_file(number)
                except ValueError:
                    print("Пожалуйста, вводите только числа.")
                except Exception as e:
                    print(e)
                    break

            if self.current_sum >= self.TARGET_SUM:
                print("Вы успешно выполнили условие для выхода из порочного цикла!")

        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")

if __name__ == "__main__":
    lucky_number = LuckyNumber()
    lucky_number.run()
