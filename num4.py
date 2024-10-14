class ScoreLimitExceededError(Exception):
    """Пользовательское исключение для ограничения максимального количества очков."""
    def __init__(self, message="Превышен лимит очков (1000)."):
        self.message = message
        super().__init__(self.message)

class GameScore:
    MAX_SCORE = 1000  # Максимальное количество очков

    def __init__(self):
        """Инициализация класса с начальным количеством очков."""
        self.score = 0

    def add_score(self, points):
        """Добавление очков игроку."""
        if self.score + points > self.MAX_SCORE:
            raise ScoreLimitExceededError(f"Нельзя добавить {points} очков. Лимит 1000 очков.")
        self.score += points
        print(f"Добавлено {points} очков. Текущий счет: {self.score}.")

    def subtract_score(self, points):
        """Уменьшение очков игрока."""
        if self.score - points < 0:
            raise ValueError("Очки не могут быть отрицательными.")
        self.score -= points
        print(f"Вычтено {points} очков. Текущий счет: {self.score}.")

    def get_score(self):
        """Возвращает текущий счет игрока."""
        return self.score

if __name__ == "__main__":
    game_score = GameScore()

    try:
        # Добавляем и вычитаем очки с проверкой исключений
        game_score.add_score(500)  # Добавить 500 очков
        game_score.add_score(600)  # Попытка добавить 600 очков (превышает лимит)
    except ScoreLimitExceededError as e:
        print(e)

    try:
        game_score.subtract_score(100)  # Вычесть 100 очков
        game_score.subtract_score(500)  # Попытка вычесть больше, чем доступно
    except ValueError as e:
        print(e)

    print(f"Конечный счет игрока: {game_score.get_score()}")
