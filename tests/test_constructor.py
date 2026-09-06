from helpers import wait_constructor
from locators import MainPageLocators


class TestConstructor:

    def test_switch_to_buns_section(self, driver):
        wait_constructor(driver)

        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        driver.find_element(*MainPageLocators.BUNS_TAB).click()

        buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)

        assert "current" in buns_tab.get_attribute("class")

    def test_switch_to_sauces_section(self, driver):
        wait_constructor(driver)

        driver.find_element(*MainPageLocators.SAUCES_TAB).click()

        sauces_tab = driver.find_element(*MainPageLocators.SAUCES_TAB)

        assert "current" in sauces_tab.get_attribute("class")

    def test_switch_to_fillings_section(self, driver):
        wait_constructor(driver)

        driver.find_element(*MainPageLocators.FILLINGS_TAB).click()

        fillings_tab = driver.find_element(*MainPageLocators.FILLINGS_TAB)

        assert "current" in fillings_tab.get_attribute("class")
