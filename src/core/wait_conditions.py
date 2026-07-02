from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.core.core_utils.config_manger import ConfigManager
from src.core.browser.browser import Browser
from src.core.core_models.locator import Locator
from src.core.logger.logger import Logger

class WaitConditions:

    @classmethod
    def _get_wait(cls, timeout: int = None):
        timeout = timeout or ConfigManager.config().timeout
        Logger.debug(f"Создание WebDriverWait с таймаутом: {timeout}с")
        return WebDriverWait(Browser.driver(), timeout)

    @classmethod
    def wait_visibility(cls, locator: Locator, timeout: int = None):
        Logger.debug(f"Ожидание видимости элемента: {locator}")
        result = cls._get_wait(timeout).until(
            EC.visibility_of_element_located(locator.selenium_tuple)
        )
        return result

    @classmethod
    def wait_invisibility(cls, locator: Locator, timeout: int = None):
        Logger.debug(f"Ожидание невидимости элемента: {locator}")
        result = cls._get_wait(timeout).until(
            EC.invisibility_of_element(locator.selenium_tuple)
        )
        return result

    @classmethod
    def wait_clickable(cls, locator: Locator, timeout: int = None):
        Logger.debug(f"Ожидание кликабельности элемента: {locator}")
        result = cls._get_wait(timeout).until(
            EC.element_to_be_clickable(locator.selenium_tuple)
        )
        return result

    @classmethod
    def wait_for_attribute_value(cls, locator: Locator, attribute: str, value: str, timeout: int = None):
        Logger.debug(f"Ожидание значения атрибута '{attribute}' = '{value}' у элемента: {locator}")
        result = cls._get_wait(timeout).until(
            EC.text_to_be_present_in_element_attribute(locator.selenium_tuple, attribute, value)
        )
        return result