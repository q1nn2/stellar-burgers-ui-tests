from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import REGISTER_URL, USER_NAME
from generators import generate_login, generate_password
from locators import AuthLocators, RegistrationLocators

WAIT_TIME = 10


def test_successful_registration(driver):
    email = generate_login()
    password = generate_password(8)

    driver.get(REGISTER_URL)

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(RegistrationLocators.NAME_INPUT)
    )

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(USER_NAME)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    login_title = WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(AuthLocators.LOGIN_TITLE)
    )

    assert login_title.text == "Вход"


def test_registration_with_short_password_shows_error(driver):
    email = generate_login()
    short_password = generate_password(5)

    driver.get(REGISTER_URL)

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(RegistrationLocators.NAME_INPUT)
    )

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(USER_NAME)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(short_password)
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    error = WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR)
    )

    assert "Некорректный пароль" in error.text
