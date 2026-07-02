from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass
class Locator:
    by: By
    value: str

    @property
    def selenium_tuple(self):
        return self.by, self.value

    @staticmethod
    def by_class_name(value: str) -> "Locator":
        return Locator(By.CLASS_NAME, value) # type: ignore[arg-type]

    @staticmethod
    def by_id(value: str) -> "Locator":
        return Locator(By.ID, value)  # type: ignore[arg-type]

    @staticmethod
    def by_xpath(value: str) -> "Locator":
        return Locator(By.XPATH, value) # type: ignore[arg-type]


