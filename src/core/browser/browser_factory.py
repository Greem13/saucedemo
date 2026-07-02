from abc import ABC, abstractmethod, ABCMeta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from src.core.logger.logger import Logger
from src.core.core_utils.config_manger import ConfigManager

class BrowserRegistry(ABCMeta):
    browsers = {}

    def __new__(mcs, name, bases, namespace, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace)
        browser_name = getattr(cls, 'name', None)
        if browser_name and browser_name not in mcs.browsers:
            mcs.browsers[browser_name] = cls
        return cls

class BaseBrowser(ABC, metaclass=BrowserRegistry):
    name = None

    @staticmethod
    @abstractmethod
    def create_driver(driver_options, page_load_strategy):
        pass

class ChromeFactory(BaseBrowser):
    name = 'chrome'

    @staticmethod
    def create_driver(driver_options, page_load_strategy):
        Logger.debug("Создание Chrome драйвера")
        options = ChromeOptions()
        options.page_load_strategy = page_load_strategy
        Logger.debug("Добавляем настройки")
        for arg in driver_options:
            options.add_argument(arg)
            Logger.debug(f"Добавлена настройка: {arg}")
        service = ChromeService()
        return webdriver.Chrome(service=service, options=options)

class FirefoxFactory(BaseBrowser):
    name = 'firefox'

    @staticmethod
    def create_driver(driver_options, page_load_strategy):
        Logger.info("Создание Firefox драйвера")
        options = FirefoxOptions()
        options.page_load_strategy = page_load_strategy
        Logger.debug("Добавляем настройки")
        for arg in driver_options:
            options.add_argument(arg)
            Logger.debug(f"Добавлена настройка: {arg}")
        Logger.debug("Добавляем приватный режим")
        firefox_profile = ConfigManager.config().firefox_profile
        for key, value in firefox_profile.items():
            options.set_preference(key, value)
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        return driver

class BrowserFactory:

    @staticmethod
    def create(browser_name, driver_options, page_load_strategy) -> webdriver.Remote:
        browser_class = BrowserRegistry.browsers.get(browser_name)
        if not browser_class:
            Logger.error(f"Неподдерживаемый браузер: {browser_name}")
            Logger.debug(f"Доступные браузеры: {list(BrowserRegistry.browsers.keys())}")
            raise ValueError(f"Unsupported browser: {browser_name}")
        return browser_class.create_driver(driver_options, page_load_strategy)