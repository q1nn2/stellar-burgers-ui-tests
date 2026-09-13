from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Timeouts, Urls
from helpers import assert_user_is_logged_in, login
from locators import AuthLocators, MainPageLocators


class TestLogin:

    def test_login_from_main_page(self, driver, registered_user):
        email, password = registered_user

        driver.get(Urls.BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()

        login(driver, email, password)
        assert_user_is_logged_in(driver)

    def test_login_from_personal_account_button(self, driver, registered_user):
        email, password = registered_user

        driver.get(Urls.BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.LOGIN_TITLE
            )
        )

        login(driver, email, password)
        assert_user_is_logged_in(driver)

    def test_login_from_registration_form(self, driver, registered_user):
        email, password = registered_user

        driver.get(Urls.REGISTER_URL)

        WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(AuthLocators.LOGIN_LINK)
        ).click()

        login(driver, email, password)
        assert_user_is_logged_in(driver)

    def test_login_from_forgot_password_form(self, driver, registered_user):
        email, password = registered_user

        driver.get(Urls.FORGOT_PASSWORD_URL)

        WebDriverWait(driver, Timeouts.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(AuthLocators.LOGIN_LINK)
        ).click()

        login(driver, email, password)
        assert_user_is_logged_in(driver)
