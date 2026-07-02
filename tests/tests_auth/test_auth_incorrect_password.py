import allure
import pytest
from src.pages.auth_page.auth_page import AuthorizationPage
from src.services.auth_service import AuthService
from src.utils.data_test_manager import DataTestManager
from src.core.logger.logger import Logger
from src.builders.user_builder import UserBuilder

data = DataTestManager.data()
usernames = [user.username for user in data.users]

@allure.epic("Модуль авторизации")
@allure.feature("Авторизация")
class TestAuthIncorrectPassword:

    @pytest.mark.parametrize(
        "user_with_invalid_password",
        [UserBuilder().with_specific_username(username).with_random_password().build() for username in usernames],
        ids=usernames
    )
    @allure.story("Неуспешная авторизация")
    @allure.title("TC-03: Авторизация с правильным логином и неверным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_auth_with_incorrect_password_and_correct_username(self, user_with_invalid_password):
        test_case_name = "TC-03: Авторизация с правильным логином и неверным паролем"

        Logger.info(f"=== {test_case_name} ===")
        Logger.info(f"👤 Пользователь: {user_with_invalid_password.username}")

        with allure.step("Шаг 1. Переходим на страницу авторизации"):
            Logger.info("Шаг 1. Переходим на страницу авторизации")
            auth_page = AuthorizationPage()
            assert auth_page.wait_load(), "Страница авторизации не загрузилась"
            Logger.info("✓ Страница авторизации загружена")

        with allure.step(f"Шаг 2. Выполняем логин с правильным логином и неверным паролем"):
            Logger.info(f"Шаг 2. Выполняем логин с правильным логином и неверным паролем")
            auth_service = AuthService()
            auth_service.login(user_with_invalid_password)

        with allure.step("Шаг 3. Проверяем появление сообщения об ошибке"):
            Logger.info("Шаг 3. Проверяем появление сообщения об ошибке")
            assert auth_page.is_error_message(), "Сообщение об ошибке авторизации не появилось"
            Logger.info("✓ Сообщение об ошибке появилось")

        with allure.step("Шаг 4. Проверяем текст сообщения об ошибке"):
            Logger.info("Шаг 4. Проверяем текст сообщения об ошибке")
            error_message = auth_page.error_message
            expected_message = DataTestManager.data().error_message
            assert error_message == expected_message, f"Сообщение об ошибке не {expected_message}, а {error_message}"
            Logger.info(f"✓ Текст сообщения соответствует ожидаемому: '{expected_message}'")