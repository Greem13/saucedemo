from src.core.form import Form
from src.core.core_models.locator import Locator
from src.core.elements.factory.element_factory import ElementFactory
from src.core.logger.logger import Logger

class BasePage(Form):
    _element_factory = ElementFactory()

    def __init__(self, locator: Locator, name: str):
        Logger.debug(f"Инициализация страницы: {name}")
        super().__init__(locator, name)
        self._page_element = self._element_factory.get_label(locator, name)

    def wait_load(self):
        Logger.debug(f"Ожидание загрузки страницы: {self._name}")
        result = self._page_element.is_displayed()
        Logger.debug(f"Страница {self._name} загружена")
        return result