from src.pages.base_page.base_page import BasePage
from src.core.core_models.locator import Locator
from src.core.logger.logger import Logger

class ShoppingCartPage(BasePage):
    def __init__(self):
        super().__init__(Locator.by_id("cart_contents_container"), "Страница корзины")
        self._continue_shopping_button = self._element_factory.get_button(Locator.by_id("continue-shopping"), "Кнопка входа из корзины")
        self._button_checkout = self._element_factory.get_button(Locator.by_id("checkout"), "Кнопка Checkout")
        Logger.debug("Страница корзины инициализирована")

    def continue_shopping(self):
        Logger.debug("Нажатие кнопки Continue Shopping")
        self._continue_shopping_button.click_button()

    def checkout(self):
        Logger.debug("Нажатие кнопки Checkout")
        self._button_checkout.click_button()

    def _get_item_label(self, item_name):
        Logger.debug(f"Поиск товара в корзине: {item_name}")
        xpath = f"//*[text()='{item_name}']"
        return self._element_factory.get_label(
            Locator.by_xpath(xpath), "Товар в корзине"
        )

    def is_item_present(self, item_name):
        Logger.debug(f"Проверка наличия товара в корзине: {item_name}")
        item_label = self._get_item_label(item_name)
        result = item_label.is_displayed()
        return result

    def item_not_present(self, item_name):
        Logger.debug(f"Проверка отсутствия товара в корзине: {item_name}")
        item_label = self._get_item_label(item_name)
        result = item_label.not_displayed()
        return result

    def remove_item(self, item_name):
        Logger.debug(f"Удаление товара из корзины: {item_name}")
        xpath = f"//*[text()='{item_name}']/ancestor::*[@class='cart_item_label']//button"
        remove_button = self._element_factory.get_button(
            Locator.by_xpath(xpath), "Кнопка удаления товара из корзины"
        )
        remove_button.click_button()