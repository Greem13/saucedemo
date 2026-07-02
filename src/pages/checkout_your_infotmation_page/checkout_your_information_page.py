from src.pages.base_page.base_page import BasePage
from src.core.core_models.locator import Locator
from src.core.elements.input import Input
from src.core.logger.logger import Logger

class CheckoutYourInformationPage(BasePage):
    def __init__(self):
        super().__init__(Locator.by_xpath("//*[text()='Checkout: Your Information']"), "Страница данных получателя для оформления заказа")
        self._first_name_input = self._element_factory.get_input(Locator.by_id("first-name"), "Поле для заполенния имени")
        self._last_name_input = self._element_factory.get_input(Locator.by_id("last-name"), "Поле для заполнения фамилии")
        self._postcode = self._element_factory.get_input(Locator.by_id("postal-code"), "Поле для заполнения")
        self._continue_button = self._element_factory.get_button(Locator.by_id("continue"), "Кнопка Continue после заполнения данных получателя")
        Logger.debug("Страница заполнения данных получателя инициализирована")

    @staticmethod
    def _enter_field(field: Input, value: str):
        Logger.debug("Очистка поля и ввод значения")
        field.clear_input()
        field.send(value)

    def enter_first_name(self, first_name: str):
        Logger.debug(f"Ввод имени: {first_name}")
        self._enter_field(self._first_name_input, first_name)

    def enter_last_name(self, last_name: str):
        Logger.debug(f"Ввод фамилии: {last_name}")
        self._enter_field(self._last_name_input, last_name)

    def enter_postcode(self, postcode: str):
        Logger.debug(f"Ввод почтового индекса: {postcode}")
        self._enter_field(self._postcode, postcode)

    def continue_checkout(self):
        Logger.debug("Нажатие кнопки Continue")
        self._continue_button.click_button()