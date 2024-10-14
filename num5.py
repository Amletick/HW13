class NameError(Exception):
    """Пользовательское исключение для ошибки валидации имени."""

    def __init__(self,
                 message="Имя должно состоять как минимум из двух слов, каждое из которых начинается с заглавной буквы."):
        self.message = message
        super().__init__(self.message)


class EmailError(Exception):
    """Пользовательское исключение для ошибки валидации email."""

    def __init__(self,
                 message="Неверный формат email. Электронная почта должна содержать символ '@' и точку '.' после '@'."):
        self.message = message
        super().__init__(self.message)


class AgeError(Exception):
    """Пользовательское исключение для ошибки валидации возраста."""

    def __init__(self, message="Возраст должен быть положительным целым числом в диапазоне от 0 до 120 лет."):
        self.message = message
        super().__init__(self.message)


class User:
    def __init__(self, name, email, age):
        """Инициализация класса с проверкой вводимых данных."""
        self.name = name
        self.email = email
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        """Проверка на то, что имя состоит минимум из двух слов с заглавными буквами."""
        words = value.split()
        if len(words) < 2 or not all(word[0].isupper() and word.isalpha() for word in words):
            raise NameError()
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        """Проверка правильности email (наличие '@' и '.' после '@')."""
        if '@' not in value or '.' not in value.split('@')[-1]:
            raise EmailError()
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        """Проверка возраста (должен быть положительным целым числом и в диапазоне от 0 до 120)."""
        if not isinstance(value, int) or value < 0 or value > 120:
            raise AgeError()
        self._age = value


if __name__ == "__main__":
    try:
        # Пример правильного ввода
        user1 = User("Иван Иванов", "ivan.ivanov@example.com", 30)
        print(f"Пользователь {user1.name}, email: {user1.email}, возраст: {user1.age}")

        # Пример с ошибкой в имени
        user2 = User("иван", "ivan.ivanov@example.com", 30)
    except (NameError, EmailError, AgeError) as e:
        print(e)

    try:
        # Пример с ошибкой в email
        user3 = User("Иван Иванов", "ivan.ivanovexample.com", 30)
    except (NameError, EmailError, AgeError) as e:
        print(e)

    try:
        # Пример с ошибкой в возрасте
        user4 = User("Иван Иванов", "ivan.ivanov@example.com", 130)
    except (NameError, EmailError, AgeError) as e:
        print(e)
