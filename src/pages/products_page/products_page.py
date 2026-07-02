from src.pages.base_page.base_page import BasePage
from src.core.core_models.locator import Locator
from src.pages.products_page.forms.side_menu import SideMenu
from src.core.elements.button import Button
from src.core.logger.logger import Logger

class ProductsPage(BasePage):
    def __init__(self):
        super().__init__(Locator.by_id('inventory_container'), "Страница с вещами")
        self._side_menu = SideMenu()
        self._side_menu_button = self._element_factory.get_button(Locator.by_id("react-burger-menu-btn"), "Кнопка бокового меню")
        self._shopping_cart_counter = self. _element_factory.get_button(Locator.by_class_name("shopping_cart_badge"), "Счетчик корзины")
        self._shopping_cart_button = self._element_factory.get_button(Locator.by_id("shopping_cart_container"), "Кнопка корзины")
        Logger.debug("Страница товаров инициализирована")

    def is_shopping_cart_counter_displayed(self) -> bool:
        Logger.debug("Проверка отображения счетчика корзины")
        result = self._shopping_cart_counter.is_displayed()
        return result

    def shopping_cart_counter_not_displayed(self) -> bool:
        Logger.debug("Проверка отсутствия счетчика корзины")
        result = self._shopping_cart_counter.not_displayed()
        return result

    @property
    def shopping_cart_count(self) -> int:
        Logger.debug("Получение количества товаров в корзине")
        if self.is_shopping_cart_counter_displayed():
            count = int(self._shopping_cart_counter.element_text)
            Logger.debug(f"Количество товаров в корзине: {count}")
            return count
        Logger.debug("Счетчик не отображается, возвращаем 0")
        return 0

    def open_side_menu(self) -> SideMenu:
        Logger.debug("Открытие бокового меню")
        self._side_menu_button.click_button()
        return self._side_menu

    def _get_add_or_remove_item_button(self, item_name, action: str) -> Button:
        Logger.debug(f"Поиск кнопки '{action}' для товара: {item_name}")
        xpath = f"//*[text()='{item_name}']/ancestor::*[@class='inventory_item_description']//button[text()='{action}']"
        button = self._element_factory.get_button(
            Locator.by_xpath(xpath),
            f"Кнопка {action} для товара: {item_name}"
        )
        return button

    def add_item(self, item_name: str):
        Logger.debug(f"Добавление товара в корзину: {item_name}")
        action = "Add to cart"
        self._get_add_or_remove_item_button(item_name, action).click_button()

    def remove_item(self, item_name: str):
        Logger.debug(f"Удаление товара из корзины: {item_name}")
        action = "Remove"
        self._get_add_or_remove_item_button(item_name, action).click_button()

    def open_shopping_cart(self):
        Logger.debug("Открытие корзины")
        self._shopping_cart_button.click_button()