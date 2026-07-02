from src.pages.base_page.base_page import BasePage
from src.core.core_models.locator import Locator
from src.core.elements.input import Input
from src.core.logger.logger import Logger

class AuthorizationForm(BasePage):
    def __init__(self):
        super().__init__(Locator.by_id('login_button_container'), 'Форма авторизации')
        self._input_username = self._element_factory.get_input(Locator.by_id('user-name'), "Поле для ввода логина")
        self._input_password = self._element_factory.get_input(Locator.by_id('password'), 'Поле для ввода пароля')
        self._login_button = self._element_factory.get_button(Locator.by_id('login-button'), "Кнопка авторизации")
        Logger.debug("Форма авторизации инициализирована")

    @staticmethod
    def _enter_field(field: Input, value: str):
        Logger.debug(f"Очистка поля и ввод значения")
        field.clear_input()
        field.send(value)

    def enter_username(self, username: str):
        Logger.debug(f"Ввод логина")
        self._enter_field(self._input_username, username)

    def enter_password(self, password: str):
        Logger.debug("Ввод пароля")
        self._enter_field(self._input_password, password)

    def login(self):
        Logger.debug("Нажатие кнопки Login")
        self._login_button.click_button()