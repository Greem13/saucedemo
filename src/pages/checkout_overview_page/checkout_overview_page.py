from src.pages.base_page.base_page import BasePage
from src.core.core_models.locator import Locator
from src.core.logger.logger import Logger

class CheckoutOverviewPage(BasePage):
    def __init__(self):
        super().__init__(Locator.by_xpath("//*[text()='Checkout: Overview']"), "Страница оформления заказа")
        self._finish_button = self._element_factory.get_button(Locator.by_id("finish"), "Кнопка заверщения оформления заказа")
        Logger.debug("Страница обзора заказа инициализирована")

    def is_item_present(self, item_name):
        Logger.debug(f"Проверка наличия товара на странице: {item_name}")
        item = self._element_factory.get_label(Locator.by_xpath(f"//*[text()='{item_name}']"), f"Добавленный товар на странице: {self._name}")
        result = item.is_displayed()
        return result

    def finish(self):
        Logger.debug("Нажатие кнопки Finish")
        self._finish_button.click_button()