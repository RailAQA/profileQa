from selenium import webdriver
import pytest

# Фикстура для всех автотестов
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()