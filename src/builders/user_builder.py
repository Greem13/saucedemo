from src.models.data_test.user_model import User
from src.utils.data_generator import DataGenerator
from src.core.logger.logger import Logger

class UserBuilder:

    def __init__(self):
        self._username = None
        self._password = None

    def with_specific_username(self, username: str):
        Logger.debug(f"Установка конкретного имени пользователя: {username}")
        self._username = username
        return self

    def with_specific_password(self, password: str):
        Logger.debug("Установка конкретного пароля")
        self._password = password
        return self

    def with_random_username(self):
        Logger.debug(f"Генерация случайного имени пользователя")
        self._username = DataGenerator.get_user_name()
        return self

    def with_random_password(self):
        Logger.debug("Генерация случайного пароля")
        self._password = DataGenerator.get_password()
        return self

    def build(self) -> User:
        if self._username is None or self._password is None:
            Logger.error("Попытка собрать User без username или password")
            raise ValueError("Username and password must be set before build()")

        Logger.debug(f"Сборка User: {self._username}")
        return User(username=self._username, password=self._password)