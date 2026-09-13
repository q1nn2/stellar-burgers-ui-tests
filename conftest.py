import pytest
from selenium import webdriver

from helpers import register_new_user


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.set_window_size(1440, 1000)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user(driver):
    return register_new_user(driver)
