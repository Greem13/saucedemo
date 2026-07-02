from src.pages.auth_page.auth_page import AuthorizationPage
from src.models.data_test.user_model import User
from src.core.logger.logger import Logger

class AuthService:

    def __init__(self):
        self._auth_page = AuthorizationPage()

    def login(self, user: User):
        Logger.debug(f"Попытка логина для пользователя: {user.username}")
        auth_form = self._auth_page.authorization_form

        auth_form.enter_username(user.username)
        Logger.debug("Имя пользователя введено")

        auth_form.enter_password(user.password)
        Logger.debug("Пароль введен")

        auth_form.login()
        Logger.debug("Нажата кнопка Login")