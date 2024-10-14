import os

CHAT_FILE = "chat.txt"


def display_chat():
    """Функция для отображения текущих сообщений чата"""
    try:
        with open(CHAT_FILE, "r", encoding="utf-8") as chat_file:
            messages = chat_file.read()
            if messages:
                print("\n=== Текущий чат ===")
                print(messages)
            else:
                print("\nЧат пока пуст.")
    except FileNotFoundError:
        print("\nЧат пока пуст.")


def send_message(user_name):
    """Функция для отправки сообщения в чат"""
    message = input("Введите ваше сообщение: ")
    with open(CHAT_FILE, "a", encoding="utf-8") as chat_file:
        chat_file.write(f"{user_name}: {message}\n")
    print("Сообщение отправлено!")


def chat():
    """Основная функция чата"""
    user_name = input("Введите ваше имя: ")
    print(f"Добро пожаловать в чат, {user_name}!")

    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть текущий текст чата")
        print("2. Отправить сообщение")
        print("3. Выйти из чата")

        choice = input("Ваш выбор: ")

        if choice == "1":
            display_chat()
        elif choice == "2":
            send_message(user_name)
        elif choice == "3":
            print("Выход из чата. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    chat()
