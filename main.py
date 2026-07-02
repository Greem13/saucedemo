import time

from src.core.browser.browser import Browser
from src.services.auth_service import AuthService
from selenium.webdriver.common.by import By

browser = Browser.driver()
browser.get("https://www.saucedemo.com/")
auth = AuthService()

auth.login()

cart = browser.find_element(By.XPATH, "//*[text()='Sauce Labs Bike Light']/ancestor::*[@class='inventory_item_description']")
add_cart_button = cart.find_element(By.XPATH, ".//button[text()='Add to cart']")

add_cart_button.click()
time.sleep(5)

browser.quit()
