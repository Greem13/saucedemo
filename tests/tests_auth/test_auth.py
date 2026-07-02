import allure
import pytest
from src.pages.auth_page.auth_page import AuthorizationPage
from src.pages.products_page.products_page import ProductsPage
from src.services.auth_service import AuthService
from src.utils.data_test_manager import DataTestManager
from src.core.logger.logger import Logger

data = DataTestManager.data()

@allure.epic("Модуль авторизации")
@allure.feature("Авторизация")
class TestAuthorization:

    @pytest.mark.parametrize(
        "user",
        [
            pytest.param(user, marks=pytest.mark.xfail)
            if user.locked_out
            else user for user in data.users
        ],
        ids=[user.username for user in data.users]
    )
    @allure.story("Логин и выход")
    @allure.title("TC-01: Авторизация и выход из системы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_and_logout(self, user):
        test_case_name = "TC-01: Авторизация и выход из системы"

        Logger.info(f"=== {test_case_name} ===")
        Logger.info(f"👤 Пользователь: {user.username} (заблокирован: {user.locked_out})")

        with allure.step("Шаг 1. Переходим на страницу авторизации"):
            Logger.info("Шаг 1. Переходим на страницу авторизации")
            auth_page = AuthorizationPage()
            assert auth_page.wait_load(), "Страница авторизации не загрузилась"
            Logger.info("✓ Страница авторизации загружена")

        with allure.step(f"Шаг 2. Выполняем логин для пользователя: {user.username}"):
            Logger.info(f"Шаг 2. Выполняем логин для пользователя: {user.username}")
            auth_service = AuthService()
            auth_service.login(user)

        with allure.step("Шаг 3. Проверяем загрузку страницы с товарами"):
            Logger.info("Шаг 3. Проверяем загрузку страницы с товарами")
            products_page = ProductsPage()
            assert products_page.wait_load(), "Страница с вещами не загрузилась"
            Logger.info("✓ Страница с товарами загружена")

        with allure.step("Шаг 4. Открываем боковое меню"):
            Logger.info("Шаг 4. Открываем боковое меню")
            side_menu = products_page.open_side_menu()
            assert side_menu.is_open(), "Боковое меню не открылось"
            Logger.info("✓ Боковое меню открыто")

        with allure.step("Шаг 5. Выполняем выход из системы"):
            Logger.info("Шаг 5. Выполняем выход из системы")
            side_menu.logout()
            assert auth_page.wait_load(), "Разлогирование не произошло, страница авторизации не загрузилась"
            Logger.info("✓ Выход из системы выполнен успешно")