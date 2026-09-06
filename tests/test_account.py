from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Timeouts
from helpers import authorize_user
from locators import AccountLocators, AuthLocators, MainPageLocators


class TestAccount:

    def test_open_personal_account(self, driver):
        authorize_user(driver)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        assert WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(
                AccountLocators.LOGOUT_BUTTON
            )
        ).is_displayed()

    def test_go_from_account_to_constructor_by_constructor_link(self, driver):
        authorize_user(driver)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(
                AccountLocators.LOGOUT_BUTTON
            )
        )

        driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()

        assert WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.CONSTRUCTOR_TITLE
            )
        ).is_displayed()

    def test_go_from_account_to_constructor_by_logo(self, driver):
        authorize_user(driver)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(
                AccountLocators.LOGOUT_BUTTON
            )
        )

        driver.find_element(*MainPageLocators.LOGO).click()

        assert WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.CONSTRUCTOR_TITLE
            )
        ).is_displayed()

    def test_logout_from_personal_account(self, driver):
        authorize_user(driver)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(
                AccountLocators.LOGOUT_BUTTON
            )
        ).click()

        assert WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.LOGIN_TITLE
            )
        ).is_displayed()
