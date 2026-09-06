from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL
from locators import MainPageLocators

WAIT_TIME = 10


def wait_constructor(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
    )


def test_switch_to_buns_section(driver):
    wait_constructor(driver)

    driver.find_element(*MainPageLocators.SAUCES_TAB).click()
    driver.find_element(*MainPageLocators.BUNS_TAB).click()

    buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)

    assert "current" in buns_tab.get_attribute("class")


def test_switch_to_sauces_section(driver):
    wait_constructor(driver)

    driver.find_element(*MainPageLocators.SAUCES_TAB).click()

    sauces_tab = driver.find_element(*MainPageLocators.SAUCES_TAB)

    assert "current" in sauces_tab.get_attribute("class")


def test_switch_to_fillings_section(driver):
    wait_constructor(driver)

    driver.find_element(*MainPageLocators.FILLINGS_TAB).click()

    fillings_tab = driver.find_element(*MainPageLocators.FILLINGS_TAB)

    assert "current" in fillings_tab.get_attribute("class")
