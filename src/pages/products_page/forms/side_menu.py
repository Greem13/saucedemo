from src.pages.base_page.base_page import BasePage
from src.core.core_models.locator import Locator
from src.pages.products_page.forms.aria_hidden import AriaHidden
from src.core.logger.logger import Logger

class SideMenu(BasePage):
    def __init__(self):
        super().__init__(Locator.by_class_name("bm-menu-wrap"), "Боковое меню")
        self._logout_button = self._element_factory.get_button(Locator.by_id("logout_sidebar_link"), "Форма бокового меню")
        self._aria_hidden = "aria-hidden"
        Logger.debug("Боковое меню инициализировано")

    def logout(self):
        Logger.debug("Выполнение выхода из системы через боковое меню")
        self._logout_button.click_button()

    def is_open(self) -> bool:
        Logger.debug("Проверка состояния бокового меню (открыто/закрыто)")
        result = self._page_element.is_attribute_value(self._aria_hidden, AriaHidden.OPENED)
        return result