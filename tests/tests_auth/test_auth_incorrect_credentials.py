import allure
from src.pages.auth_page.auth_page import AuthorizationPage
from src.services.auth_service import AuthService
from src.builders.user_builder import UserBuilder
from src.utils.data_test_manager import DataTestManager
from src.core.logger.logger import Logger

@allure.epic("Модуль авторизации")
@allure.feature("Авторизация")
class TestAuthIncorrectCredentials:

    @allure.story("Неуспешная авторизация")
    @allure.title("TC-02: Авторизация с неверными учетными данными")
    @allure.severity(allure.severity_level.NORMAL)
    def test_auth_with_incorrect_password_and_username(self):
        test_case_name = "TC-02: Авторизация с неверными учетными данными"

        Logger.info(f"=== {test_case_name} ===")

        with allure.step("Шаг 1. Переходим на страницу авторизации"):
            Logger.info("Шаг 1. Переходим на страницу авторизации")
            auth_page = AuthorizationPage()
            assert auth_page.wait_load(), "Страница авторизации не загрузилась"
            Logger.info("✓ Страница авторизации загружена")

        with allure.step("Шаг 2. Генерируем случайные невалидные учетные данные"):
            Logger.info("Шаг 2. Генерируем случайные невалидные учетные данные")
            invalid_user = UserBuilder().with_random_password().with_random_username().build()
            Logger.info(f"👤 Сгенерированный пользователь: {invalid_user.username}:{invalid_user.password}")

        with allure.step("Шаг 3. Выполняем попытку логина с невалидными данными"):
            Logger.info("Шаг 3. Выполняем попытку логина с невалидными данными")
            auth_service = AuthService()
            auth_service.login(invalid_user)

        with allure.step("Шаг 4. Проверяем появление сообщения об ошибке"):
            Logger.info("Шаг 4. Проверяем появление сообщения об ошибке")
            assert auth_page.is_error_message(), "Сообщение об ошибке авторизации не появилось"
            Logger.info("✓ Сообщение об ошибке появилось")

        with allure.step("Шаг 5. Проверяем текст сообщения об ошибке"):
            Logger.info("Шаг 5. Проверяем текст сообщения об ошибке")
            error_message = auth_page.error_message
            expected_message = DataTestManager.data().error_message
            assert error_message == expected_message, f"Сообщение об ошибке не {expected_message}, а {error_message}"
            Logger.info(f"✓ Текст сообщения соответствует ожидаемому: '{expected_message}'")