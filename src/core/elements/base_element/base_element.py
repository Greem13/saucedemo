from src.core.form import Form
from src.core.wait_conditions import WaitConditions
from selenium.common.exceptions import TimeoutException
from abc import ABC
from selenium.webdriver.remote.webelement import WebElement
from src.core.js_actions import JavaScriptActions
from src.core.logger.logger import Logger


class BaseElement(Form, ABC):
    _conditions = WaitConditions()
    _js_actions = JavaScriptActions()

    def is_displayed(self) -> bool:
        Logger.debug(f"Проверка видимости элемента: {self._name}")
        try:
            self._conditions.wait_visibility(self._locator)
            Logger.debug(f"Элемент '{self._name}' видим")
            return True
        except TimeoutException:
            Logger.debug(f"Элемент '{self._name}' не видим")
            return False

    def not_displayed(self) -> bool:
        Logger.debug(f"Проверка невидимости элемента: {self._name}")
        try:
            result = self._conditions.wait_invisibility(self._locator)
            Logger.debug(f"Элемент '{self._name}' невидим: {result}")
            return result
        except TimeoutException:
            Logger.debug(f"Элемент '{self._name}' не стал невидимым")
            return False

    @property
    def element(self) -> WebElement:
        Logger.debug(f"Получение элемента: {self._name}")
        return self._conditions.wait_visibility(self._locator)

    @property
    def element_text(self) -> str:
        Logger.debug(f"Получение текста элемента: {self._name}")
        text = self.element.text
        Logger.debug(f"Текст элемента '{self._name}': {text}")
        return text

    def is_attribute_value(self, attribute, value) -> bool:
        Logger.debug(f"Проверка атрибута '{attribute}' = '{value}' у элемента: {self._name}")
        try:
            result = self._conditions.wait_for_attribute_value(self._locator, attribute, value)
            Logger.debug(f"Атрибут '{attribute}' имеет значение '{value}': {result}")
            return result
        except TimeoutException:
            Logger.debug(f"Атрибут '{attribute}' не принял значение '{value}'")
            return False