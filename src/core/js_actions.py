from src.core.browser.browser import Browser
from selenium.webdriver.remote.webelement import WebElement
from src.core.logger.logger import Logger

class JavaScriptActions:
    SCRIPT_CLICK = "arguments[0].click();"
    SCRIPT_SCROLL_TO = "arguments[0].scrollIntoView(true);"

    def click(self, element: WebElement):
        Logger.debug("Выполнение клика через JavaScript")
        Browser.driver().execute_script(self.SCRIPT_CLICK, element)

    def scroll_to(self, element: WebElement):
        Logger.debug("Скролл к элементу через JavaScript")
        Browser.driver().execute_script(self.SCRIPT_SCROLL_TO, element)