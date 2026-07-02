from src.core.elements.base_element.base_element import BaseElement
from src.core.logger.logger import Logger

class Button(BaseElement):
    def click_button(self):
        Logger.debug(f"Клик по кнопке: {self._name}")
        self._conditions.wait_clickable(self._locator).click()

    def js_click(self):
        Logger.debug(f"JavaScript клик по кнопке: {self._name}")
        self._js_actions.click(self._conditions.wait_clickable(self._locator))