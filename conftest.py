import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.set_window_size(1440, 1000)
    yield browser
    browser.quit()
