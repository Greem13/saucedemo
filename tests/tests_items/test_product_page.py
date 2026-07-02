import allure
import pytest
from src.services.auth_service import AuthService
from src.pages.auth_page.auth_page import AuthorizationPage
from src.pages.products_page.products_page import ProductsPage
from src.pages.products_page.items import Items
from src.utils.data_test_manager import DataTestManager
from src.core.logger.logger import Logger

data = DataTestManager.data()

@allure.epic("Модуль товаров")
@allure.feature("Управление товарами")
class TestProductsPage:

    @pytest.mark.parametrize(
        "user",
        [user for user in data.users if not user.locked_out],
        ids=[user.username for user in data.users if not user.locked_out]
    )
    @allure.story("Добавление и удаление товара")
    @allure.title("TC-07: Добавление и удаление товара на странице товаров")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_and_remove_item_in_products_page(self, user):
        test_case_name = "TC-07: Добавление и удаление товара на странице товаров"

        Logger.info(f"=== {test_case_name} ===")
        Logger.info(f"👤 Пользователь: {user.username}")

        with allure.step("Инициализация страниц и сервисов"):
            auth_page = AuthorizationPage()
            auth_service = AuthService()
            products_page = ProductsPage()
            item_name = Items.SAUCE_LABS_BACKPACK

        with allure.step("Шаг 1. Переходим на страницу авторизации"):
            Logger.info("Шаг 1. Переходим на страницу авторизации")
            assert auth_page.wait_load(), "Страница авторизации не загрузилась"
            Logger.info("✓ Страница авторизации загружена")

        with allure.step(f"Шаг 2. Выполняем логин для пользователя: {user.username}"):
            Logger.info(f"Шаг 2. Выполняем логин для пользователя: {user.username}")
            auth_service.login(user)

        with allure.step("Шаг 3. Проверяем загрузку страницы с товарами"):
            Logger.info("Шаг 3. Проверяем загрузку страницы с товарами")
            assert products_page.wait_load(), "Страница с картами товаров не загрузилась"
            Logger.info("✓ Страница с товарами загружена")

        with allure.step(f"Шаг 4. Добавляем товар в корзину: {item_name.value}"):
            Logger.info(f"Шаг 4. Добавляем товар в корзину: {item_name.value}")
            products_page.add_item(item_name)

        with allure.step("Шаг 5. Проверяем отображение счетчика корзины"):
            Logger.info("Шаг 5. Проверяем отображение счетчика корзины")
            assert products_page.is_shopping_cart_counter_displayed(), "Счетчик товаров в корзине не появился"
            Logger.info("✓ Счетчик корзины отображается")

        with allure.step("Шаг 6. Проверяем количество товаров в корзине"):
            Logger.info("Шаг 6. Проверяем количество товаров в корзине")
            expected_shopping_cart_count = 1
            shopping_cart_count = products_page.shopping_cart_count
            assert shopping_cart_count == expected_shopping_cart_count, f"В корзине товаров: {shopping_cart_count}, а не {expected_shopping_cart_count}"
            Logger.info(f"✓ Количество товаров в корзине: {shopping_cart_count}")

        with allure.step(f"Шаг 7. Удаляем товар из корзины: {item_name.value}"):
            Logger.info(f"Шаг 7. Удаляем товар из корзины: {item_name.value}")
            products_page.remove_item(item_name)

        with allure.step("Шаг 8. Проверяем исчезновение счетчика корзины"):
            Logger.info("Шаг 8. Проверяем исчезновение счетчика корзины")
            assert products_page.shopping_cart_counter_not_displayed(), "Счетчик товаров в корзине не исчез"
            Logger.info("✓ Счетчик корзины исчез")