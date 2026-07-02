import allure
import pytest
from src.services.auth_service import AuthService
from src.pages.auth_page.auth_page import AuthorizationPage
from src.pages.products_page.products_page import ProductsPage
from src.pages.products_page.items import Items
from src.utils.data_test_manager import DataTestManager
from src.pages.shopping_cart_page.shopping_cart_page import ShoppingCartPage
from src.pages.checkout_your_infotmation_page.checkout_your_information_page import CheckoutYourInformationPage
from src.services.checkout_service import CheckoutService
from src.pages.checkout_overview_page.checkout_overview_page import CheckoutOverviewPage
from src.pages.checkout_complete_page.checkout_complete_page import CheckoutCompletePage
from src.core.logger.logger import Logger

data = DataTestManager.data()

@allure.epic("Оформление заказа")
@allure.feature("Успешное оформление заказа")
class TestCheckoutOrder:

    @pytest.mark.parametrize(
        "user",
        [user for user in data.users if not user.locked_out],
        ids=[user.username for user in data.users if not user.locked_out]
    )
    @allure.story("Полный сценарий покупки")
    @allure.title("TC-06: Полный сценарий покупки товара")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_checkout_order(self, user):
        test_case_name = "TC-06: Полный сценарий покупки товара"

        Logger.info(f"=== {test_case_name} ===")
        Logger.info(f"👤 Пользователь: {user.username}")

        with allure.step("Инициализация страниц и сервисов"):
            auth_page = AuthorizationPage()
            auth_service = AuthService()
            products_page = ProductsPage()
            shopping_cart_page = ShoppingCartPage()
            checkout_your_information_page = CheckoutYourInformationPage()
            checkout_service = CheckoutService()
            checkout_overview_page = CheckoutOverviewPage()
            checkout_complete_page = CheckoutCompletePage()
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

        with allure.step("Шаг 8. Переходим к оформлению заказа"):
            Logger.info("Шаг 8. Переходим к оформлению заказа")
            shopping_cart_page.checkout()

        with allure.step("Шаг 9. Проверяем загрузку страницы заполнения данных"):
            Logger.info("Шаг 9. Проверяем загрузку страницы заполнения данных")
            assert checkout_your_information_page.wait_load(), "Страница для заполнения данных получателя не загрузилась"
            Logger.info("✓ Страница заполнения данных загружена")

        with allure.step("Шаг 10. Заполняем данные получателя"):
            Logger.info("Шаг 10. Заполняем данные получателя")
            checkout_info = checkout_service.fill_customer_information()
            Logger.info(
                f"✓ Данные получателя: {checkout_info.first_name} {checkout_info.last_name}, {checkout_info.postcode}")

        with allure.step("Шаг 11. Проверяем загрузку страницы обзора заказа"):
            Logger.info("Шаг 11. Проверяем загрузку страницы обзора заказа")
            assert checkout_overview_page.wait_load(), "Страница оформления заказа не загрузилась"
            Logger.info("✓ Страница обзора заказа загружена")

        with allure.step(f"Шаг 12. Проверяем наличие товара в заказе: {item_name.value}"):
            Logger.info(f"Шаг 12. Проверяем наличие товара в заказе: {item_name.value}")
            assert checkout_overview_page.is_item_present(item_name), "Товар не добавился в заказ"
            Logger.info(f"✓ Товар {item_name.value} присутствует в заказе")

        with allure.step("Шаг 13. Завершаем оформление заказа"):
            Logger.info("Шаг 13. Завершаем оформление заказа")
            checkout_overview_page.finish()
            Logger.info("✓ Заказ оформлен")

        with allure.step("Шаг 14. Проверяем загрузку страницы завершения заказа"):
            Logger.info("Шаг 14. Проверяем загрузку страницы завершения заказа")
            assert checkout_complete_page.wait_load(), "Страница с уведомлением о завершении заказа не загрузилась"
            Logger.info("✓ Страница завершения заказа загружена")

        with allure.step("Шаг 15. Возвращаемся на главную страницу"):
            Logger.info("Шаг 15. Возвращаемся на главную страницу")
            checkout_complete_page.back_home()

        with allure.step("Шаг 16. Проверяем загрузку страницы с товарами"):
            Logger.info("Шаг 16. Проверяем загрузку страницы с товарами")
            assert products_page.wait_load(), "Страница с картами товаров не загрузилась"
            Logger.info("✓ Страница с товарами загружена")