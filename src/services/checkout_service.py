from src.pages.checkout_your_infotmation_page.checkout_your_information_page import CheckoutYourInformationPage
from src.models.checkout_info_model import CheckoutInfo
from src.utils.data_generator import DataGenerator
from src.core.logger.logger import Logger

class CheckoutService:

    def __init__(self):
        self._checkout_page = CheckoutYourInformationPage()

    def fill_customer_information(self, checkout_info: CheckoutInfo = None) -> CheckoutInfo:
        if checkout_info is None:
            Logger.debug("Генерация случайных данных для оформления заказа")
            checkout_info = self._generate_random_checkout_info()

        Logger.debug(
            f"Заполнение данных получателя: {checkout_info.first_name} {checkout_info.last_name}, {checkout_info.postcode}")

        self._checkout_page.enter_first_name(checkout_info.first_name)
        Logger.debug("Имя введено")

        self._checkout_page.enter_last_name(checkout_info.last_name)
        Logger.debug("Фамилия введена")

        self._checkout_page.enter_postcode(checkout_info.postcode)
        Logger.debug("Почтовый индекс введен")

        self._checkout_page.continue_checkout()
        Logger.debug("Нажата кнопка Continue")

        return checkout_info

    @staticmethod
    def _generate_random_checkout_info() -> CheckoutInfo:
        return CheckoutInfo(
            first_name=DataGenerator.get_first_name(),
            last_name=DataGenerator.get_last_name(),
            postcode=DataGenerator.get_postcode()
        )