from src.pages.base_page.base_page import BasePage
from src.core.core_models.locator import Locator
from src.core.logger.logger import Logger

class CheckoutCompletePage(BasePage):
    def __init__(self):
        super().__init__(Locator.by_xpath("//*[text()='Checkout: Complete!']"), "Страница c уведомлением о завершении заказа")
        self._back_home_button = self._element_factory.get_button(Locator.by_id("back-to-products"), "Кнопка для возврата на главную страницу после завершения оформления заказа")
        Logger.debug("Страница завершения заказа инициализирована")

    def back_home(self):
        Logger.debug("Нажатие кнопки Back Home")
        self._back_home_button.click_button()