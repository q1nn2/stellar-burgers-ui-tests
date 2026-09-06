from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import authorize_user
from locators import AccountLocators, AuthLocators, MainPageLocators

WAIT_TIME = 10


def test_open_personal_account(driver):
    authorize_user(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    logout_button = WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(AccountLocators.LOGOUT_BUTTON)
    )

    assert logout_button.is_displayed()


def test_go_from_account_to_constructor_by_constructor_link(driver):
    authorize_user(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(AccountLocators.LOGOUT_BUTTON)
    )

    driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()

    title = WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
    )

    assert "Соберите бургер" in title.text


def test_go_from_account_to_constructor_by_logo(driver):
    authorize_user(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(AccountLocators.LOGOUT_BUTTON)
    )

    driver.find_element(*MainPageLocators.LOGO).click()

    title = WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
    )

    assert "Соберите бургер" in title.text


def test_logout_from_personal_account(driver):
    authorize_user(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.element_to_be_clickable(AccountLocators.LOGOUT_BUTTON)
    ).click()

    login_title = WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(AuthLocators.LOGIN_TITLE)
    )

    assert login_title.text == "Вход"
