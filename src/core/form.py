from src.core.core_models.locator import Locator
from abc import ABC
from src.core.logger.logger import Logger

class Form(ABC):
    def __init__(self, locator: Locator, name: str):
        Logger.debug(f"Инициализация формы: {name}")
        self._locator = locator
        self._name = name