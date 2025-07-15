from selenium import webdriver
from pages.base_page import BasePage
import pytest

def pytest_addoption(parser):
    parser.addoption('--stage', action='store', default=None, help="Choose stage: local or dev")

@pytest.fixture(scope='function')
def driver(request):
    """Фикстура для всех тестов"""
    stage = request.config.getoption("stage")
    driver = None
    
    if stage == "dev_desktop":
        """Запуск для DEV стейджа"""
        # Запуск браузера в скрытом режиме
        options_chrome = webdriver.ChromeOptions()
        options_chrome.add_argument('--headless=new')
        options_chrome.add_argument("--no-sandbox")
        options_chrome.add_argument("--window-size=1440,825")
        options_chrome.add_argument("--disable-infobars")
        options_chrome.add_argument("--disable-dev-shm-usage")
        options_chrome.add_argument("--disable-web-security")
        options_chrome.add_argument("--allow-running-insecure-content")
        options_chrome.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options_chrome)
    
    elif stage == "local_desktop":
        """Запуск на LOCAL стейдже"""
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif stage == "dev_mobile":
        """Запуск на LOCAL стейдже"""
        options_chrome = webdriver.ChromeOptions()
        options_chrome.add_argument('--headless=new')
        options_chrome.add_argument("--no-sandbox")
        options_chrome.add_argument("--window-size=415,896")
        options_chrome.add_argument("--disable-infobars")
        options_chrome.add_argument("--disable-dev-shm-usage")
        options_chrome.add_argument("--disable-web-security")
        options_chrome.add_argument("--allow-running-insecure-content")
        options_chrome.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options_chrome)
        
    elif stage == "local_mobile":
        options_chrome = webdriver.ChromeOptions()
        options_chrome.add_argument("--window-size=415,896")
        driver = webdriver.Chrome(options=options_chrome)

    else:
        """Обработка ситуации, если не указан стейдж"""
        raise pytest.UsageError("--stage should be local or dev")
    yield driver
    driver.quit()