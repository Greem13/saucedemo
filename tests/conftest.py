import pytest
from src.core.browser.browser import Browser
from src.core.core_utils.config_manger import ConfigManager
from src.core.logger.logger import Logger
import allure

@pytest.fixture(scope='function', autouse=True)
def browser(request):
    Logger.info("🚀 Запуск браузера")
    Logger.info(f"🌐 Открываем страницу: {ConfigManager.config().base_url}")
    Browser.driver().get(ConfigManager.config().base_url)
    yield
    Logger.info("🔚 Закрытие браузера")
    Browser.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        test_name = item.name
        duration = report.duration

        if report.passed:
            Logger.info(f"✅ ТЕСТ {test_name} УСПЕШНО ЗАВЕРШЕН (время: {duration:.2f}с)")
        elif report.failed:
            Logger.error(f"❌ ТЕСТ {test_name} ПРОВАЛЕН (время: {duration:.2f}с)")
            allure.attach(
                Browser.driver().get_screenshot_as_png(),
                name="Скриншот при падении",
                attachment_type=allure.attachment_type.PNG
            )
        elif report.skipped:
            Logger.warning(f"⏭️ ТЕСТ {test_name} ПРОПУЩЕН")