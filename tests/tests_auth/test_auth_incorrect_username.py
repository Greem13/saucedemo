import allure
import pytest
from src.pages.auth_page.auth_page import AuthorizationPage
from src.services.auth_service import AuthService
from src.utils.data_test_manager import DataTestManager
from src.builders.user_builder import UserBuilder
from src.core.logger.logger import Logger

data = DataTestManager.data()
passwords = [user.password for user in data.users]

@allure.epic("Модуль авторизации")
@allure.feature("Авторизация")
class TestAuthIncorrectUsername:

    @pytest.mark.parametrize(
        "user_with_incorrect_username",
        [UserBuilder().with_specific_password(password).with_random_username().build() for password in passwords],
        ids=[f"wrong_user_{i}" for i in range(len(passwords))]
    )
    @allure.story("Неуспешная авторизация")
    @allure.title("TC-04: Авторизация с неверным логином и правильным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_auth_with_correct_password_and_incorrect_username(self, user_with_incorrect_username):
        test_case_name = "TC-04: Авторизация с неверным логином и правильным паролем"

        Logger.info(f"=== {test_case_name} ===")
        Logger.info(
            f"👤 Сгенерированный пользователь: {user_with_incorrect_username.username}:{user_with_incorrect_username.password}")

        with allure.step("Шаг 1. Переходим на страницу авторизации"):
            Logger.info("Шаг 1. Переходим на страницу авторизации")
            auth_page = AuthorizationPage()
            assert auth_page.wait_load(), "Страница авторизации не загрузилась"
            Logger.info("✓ Страница авторизации загружена")

        with allure.step("Шаг 2. Выполняем логин с неверным логином и правильным паролем"):
            Logger.info("Шаг 2. Выполняем логин с неверным логином и правильным паролем")
            auth_service = AuthService()
            auth_service.login(user_with_incorrect_username)
            Logger.info("✓ Попытка логина выполнена")

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