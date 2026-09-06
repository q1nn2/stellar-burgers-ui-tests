from selenium.webdriver.support.wait import WebDriverWait

from data import Timeouts
from helpers import wait_constructor
from locators import MainPageLocators


class TestConstructor:

    def test_switch_to_buns_section(self, driver):
        wait_constructor(driver)

        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        driver.find_element(*MainPageLocators.BUNS_TAB).click()

        assert WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            lambda d: "current"
            in d.find_element(*MainPageLocators.BUNS_TAB).get_attribute("class")
        )

    def test_switch_to_sauces_section(self, driver):
        wait_constructor(driver)

        driver.find_element(*MainPageLocators.SAUCES_TAB).click()

        assert WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            lambda d: "current"
            in d.find_element(*MainPageLocators.SAUCES_TAB).get_attribute("class")
        )

    def test_switch_to_fillings_section(self, driver):
        wait_constructor(driver)

        driver.find_element(*MainPageLocators.FILLINGS_TAB).click()

        assert WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            lambda d: "current"
            in d.find_element(*MainPageLocators.FILLINGS_TAB).get_attribute("class")
        )
