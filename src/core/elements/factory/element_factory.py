from src.core.core_models.locator import Locator
from src.core.elements.base_element.base_element import BaseElement
from typing import Type, TypeVar
from src.core.elements.label import Label
from src.core.elements.input import Input
from src.core.elements.button import Button
from src.core.logger.logger import Logger

E = TypeVar('E', bound=BaseElement)


class ElementFactory:

    @staticmethod
    def _get_element(type_element: Type[E], locator: Locator, name: str) -> E:
        Logger.debug(f"Создание элемента '{name}' с локатором: {locator}")
        return type_element(locator, name)

    def get_label(self, locator: Locator, name: str) -> Label:
        Logger.debug(f"Создание Label: {name}")
        return self._get_element(Label, locator, name)

    def get_input(self, locator: Locator, name: str) -> Input:
        Logger.debug(f"Создание Input: {name}")
        return self._get_element(Input, locator, name)

    def get_button(self, locator: Locator, name: str) -> Button:
        Logger.debug(f"Создание Button: {name}")
        return self._get_element(Button, locator, name)