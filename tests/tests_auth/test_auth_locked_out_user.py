import allure
import pytest
from src.pages.auth_page.auth_page import AuthorizationPage
from src.services.auth_service import AuthService
from src.utils.data_test_manager import DataTestManager
from src.core.logger.logger import Logger

data = DataTestManager.data()
locked_out_users = [user for user in data.users if user.locked_out]

@allure.epic("Модуль авторизации")
@allure.feature("Авторизация")
class TestAuthLockedOutUser:

    @pytest.mark.parametrize(
        "locked_out_user",
        locked_out_users,
        ids=[user.username for user in locked_out_users]
    )
    @allure.story("Неуспешная авторизация")
    @allure.title("TC-05: Авторизация заблокированного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_auth_with_locked_out_user(self, locked_out_user):
        test_case_name = "TC-05: Авторизация заблокированного пользователя"

        Logger.info(f"=== {test_case_name} ===")
        Logger.info(f"👤 Пользователь: {locked_out_user.username} (заблокирован: {locked_out_user.locked_out})")

        with allure.step("Шаг 1. Переходим на страницу авторизации"):
            Logger.info("Шаг 1. Переходим на страницу авторизации")
            auth_page = AuthorizationPage()
            assert auth_page.wait_load(), "Страница авторизации не загрузилась"
            Logger.info("✓ Страница авторизации загружена")

        with allure.step(f"Шаг 2. Выполняем попытку логина для заблокированного пользователя: {locked_out_user.username}"):
            Logger.info(f"Шаг 2. Выполняем попытку логина для заблокированного пользователя: {locked_out_user.username}")
            auth_service = AuthService()
            auth_service.login(locked_out_user)
            Logger.info("✓ Попытка логина выполнена")

        with allure.step("Шаг 3. Проверяем появление сообщения об ошибке"):
            Logger.info("Шаг 3. Проверяем появление сообщения об ошибке")
            assert auth_page.is_error_message(), "Сообщение об ошибке авторизации не появилось"
            Logger.info("✓ Сообщение об ошибке появилось")

        with allure.step("Шаг 4. Проверяем текст сообщения об ошибке для заблокированного пользователя"):
            Logger.info("Шаг 4. Проверяем текст сообщения об ошибке для заблокированного пользователя")
            error_message = auth_page.error_message
            expected_message = DataTestManager.data().error_message_locked_out_user
            assert error_message == expected_message, f"Сообщение об ошибке не {expected_message}, а {error_message}"
            Logger.info(f"✓ Текст сообщения соответствует ожидаемому: '{expected_message}'")