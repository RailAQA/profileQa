from selenium import webdriver
import pytest

# Фикстура для всех автотестов
@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()