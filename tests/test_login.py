from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL, FORGOT_PASSWORD_URL, REGISTER_URL
from helpers import assert_user_is_logged_in, login, register_new_user
from locators import AuthLocators, MainPageLocators

WAIT_TIME = 10


def test_login_from_main_page(driver):
    email, password = register_new_user(driver)

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()

    login(driver, email, password)
    assert_user_is_logged_in(driver)


def test_login_from_personal_account_button(driver):
    email, password = register_new_user(driver)

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(AuthLocators.LOGIN_TITLE)
    )

    login(driver, email, password)
    assert_user_is_logged_in(driver)


def test_login_from_registration_form(driver):
    email, password = register_new_user(driver)

    driver.get(REGISTER_URL)

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.element_to_be_clickable(AuthLocators.LOGIN_LINK)
    ).click()

    login(driver, email, password)
    assert_user_is_logged_in(driver)


def test_login_from_forgot_password_form(driver):
    email, password = register_new_user(driver)

    driver.get(FORGOT_PASSWORD_URL)

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.element_to_be_clickable(AuthLocators.LOGIN_LINK)
    ).click()

    login(driver, email, password)
    assert_user_is_logged_in(driver)
