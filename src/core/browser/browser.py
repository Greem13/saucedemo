from src.core.core_utils.config_manger import ConfigManager
from src.core.logger.logger import Logger
from src.core.browser.browser_factory import BrowserFactory

class Browser:
    _driver = None

    @classmethod
    def driver(cls):
        if cls._driver is None:
            browser_name = ConfigManager.config().browser
            driver_options = ConfigManager.config().get_current_browser_options()
            page_load_strategy = ConfigManager.config().page_load_strategy

            Logger.debug(f"Имя браузера: {browser_name}")
            Logger.debug(f"Стратегия загрузки страниц: {page_load_strategy}")
            Logger.debug(f"Настройки драйвера: {driver_options}")

            cls._driver = BrowserFactory.create(browser_name, driver_options, page_load_strategy)
        return cls._driver

    @classmethod
    def quit(cls):
        if cls._driver:
            Logger.info("🔚 Закрытие браузера")
            cls._driver.quit()
            cls._driver = None