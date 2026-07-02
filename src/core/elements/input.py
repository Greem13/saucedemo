from src.core.elements.base_element.base_element import BaseElement
from src.core.logger.logger import Logger

class Input(BaseElement):

    def clear_input(self):
        Logger.debug(f"Очистка поля ввода: {self._name}")
        self.element.clear()

    def send(self, *args):
        Logger.debug(f"Ввод значения в поле: {self._name}")
        self.element.send_keys(*args)