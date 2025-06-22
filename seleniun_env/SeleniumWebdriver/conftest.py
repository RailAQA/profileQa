from selenium import webdriver
import pytest

# Фикстура для всех автотестов
@pytest.fixture(scope='session')
def driver():
    # Запуск браузера в скрытом режиме. Передаем аргумент "--headless=new"
    options_chroome = webdriver.ChromeOptions()
    options_chroome.add_argument('--headless=new')
    #
    driver = webdriver.Chrome(options=options_chroome)
    driver.maximize_window()
    yield driver
    driver.quit()