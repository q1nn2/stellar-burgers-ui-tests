from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls, UserData
from generators import generate_login, generate_password
from locators import AuthLocators, MainPageLocators, RegistrationLocators

WAIT_TIME = 10


def register_new_user(driver):
    """Регистрирует нового пользователя через UI и возвращает email и пароль."""
    email = generate_login()
    password = generate_password(8)

    driver.get(Urls.REGISTER_URL)

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(
            RegistrationLocators.NAME_INPUT
        )
    )

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(
        UserData.USER_NAME
    )
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(
            AuthLocators.LOGIN_TITLE
        )
    )

    return email, password


def login(driver, email, password):
    """Вводит email и пароль в открытую форму входа."""
    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(
            AuthLocators.EMAIL_INPUT
        )
    )

    driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.invisibility_of_element_located(
            AuthLocators.LOGIN_BUTTON
        )
    )


def assert_user_is_logged_in(driver):
    """Проверяет сохранение авторизации по кнопке «Оформить заказ» на главной."""
    driver.get(Urls.BASE_URL)

    assert WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(
            MainPageLocators.ORDER_BUTTON
        )
    ).is_displayed()


def authorize_user(driver):
    email, password = register_new_user(driver)
    login(driver, email, password)
    driver.get(Urls.BASE_URL)


def wait_constructor(driver):
    driver.get(Urls.BASE_URL)
    WebDriverWait(driver, WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(
            MainPageLocators.CONSTRUCTOR_TITLE
        )
    )
