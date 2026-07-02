from src.pages.base_page.base_page import BasePage
from src.core.core_models.locator import Locator
from src.pages.auth_page.forms.auth_form import AuthorizationForm
from src.core.logger.logger import Logger

class AuthorizationPage(BasePage):
    def __init__(self):
        super().__init__(Locator.by_class_name("login_logo"), 'Страница авторизации')
        self._accepted_usernames = self._element_factory.get_label(Locator.by_id('login_credentials'), 'допустимые логины')
        self._password = self._element_factory.get_label(Locator.by_class_name('login_password'), 'пароль для всех пользователей')
        self.authorization_form = AuthorizationForm()
        self._error_massage = self._element_factory.get_label(Locator.by_xpath("//*[@data-test='error']"), "Сообщение об ошибке")
        Logger.debug("Страница авторизации инициализирована")

    @property
    def accepted_usernames_text(self) -> str:
        Logger.debug("Получение текста допустимых логинов")
        return self._accepted_usernames.element_text

    @property
    def password_text(self) -> str:
        Logger.debug("Получение текста пароля")
        return self._password.element_text

    def is_error_message(self) -> bool:
        Logger.debug("Проверка наличия сообщения об ошибке")
        return self._error_massage.is_displayed()

    @property
    def error_message(self) -> str:
        Logger.debug("Получение текста сообщения об ошибке")
        return self._error_massage.element_text