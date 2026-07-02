import allure
import pytest
from src.services.auth_service import AuthService
from src.pages.auth_page.auth_page import AuthorizationPage
from src.pages.products_page.products_page import ProductsPage
from src.pages.products_page.items import Items
from src.utils.data_test_manager import DataTestManager
from src.pages.shopping_cart_page.shopping_cart_page import ShoppingCartPage
from src.core.logger.logger import Logger

data = DataTestManager.data()

@allure.epic("Модуль корзины")
@allure.feature("Управление корзиной")
class TestShoppingCart:

    @pytest.mark.parametrize(
        "user",
        [user for user in data.users if not user.locked_out],
        ids=[user.username for user in data.users if not user.locked_out]
    )
    @allure.story("Добавление и удаление товара")
    @allure.title("TC-08: Добавление и удаление товара в корзине")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_remove_item_in_shopping_cart_page(self, user):
        test_case_name = "TC-08: Добавление и удаление товара в корзине"

        Logger.info(f"=== {test_case_name} ===")
        Logger.info(f"👤 Пользователь: {user.username}")

        with allure.step("Инициализация страниц и сервисов"):
            auth_page = AuthorizationPage()
            auth_service = AuthService()
            products_page = ProductsPage()
            shopping_cart_page = ShoppingCartPage()
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

        with allure.step("Шаг 5. Открываем корзину"):
            Logger.info("Шаг 5. Открываем корзину")
            products_page.open_shopping_cart()

        with allure.step("Шаг 6. Проверяем загрузку страницы корзины"):
            Logger.info("Шаг 6. Проверяем загрузку страницы корзины")
            assert shopping_cart_page.wait_load(), "Страница с корзиной не загрузилась"
            Logger.info("✓ Страница корзины загружена")

        with allure.step(f"Шаг 7. Проверяем наличие товара в корзине: {item_name.value}"):
            Logger.info(f"Шаг 7. Проверяем наличие товара в корзине: {item_name.value}")
            assert shopping_cart_page.is_item_present(item_name), "Выбранный товар не добавился в корзину"
            Logger.info(f"✓ Товар {item_name.value} присутствует в корзине")

        with allure.step(f"Шаг 8. Удаляем товар из корзины: {item_name.value}"):
            Logger.info(f"Шаг 8. Удаляем товар из корзины: {item_name.value}")
            shopping_cart_page.remove_item(item_name)

        with allure.step("Шаг 9. Проверяем, что товар отсутствует в корзине"):
            Logger.info("Шаг 9. Проверяем, что товар отсутствует в корзине")
            assert shopping_cart_page.item_not_present(item_name), "Товар не удалился из корзины"
            Logger.info("✓ Товар отсутствует в корзине")

        with allure.step("Шаг 10. Продолжаем покупки"):
            Logger.info("Шаг 10. Продолжаем покупки")
            shopping_cart_page.continue_shopping()

        with allure.step("Шаг 11. Проверяем загрузку страницы с товарами"):
            Logger.info("Шаг 11. Проверяем загрузку страницы с товарами")
            assert products_page.wait_load(), "Страница с картами товаров не загрузилась"
            Logger.info("✓ Страница с товарами загружена")