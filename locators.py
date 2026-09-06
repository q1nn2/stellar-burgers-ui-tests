from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']/ancestor::a[1]")  # Ссылка «Личный кабинет»
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/ancestor::a[1]")  # Ссылка «Конструктор»
    LOGO = (By.XPATH, "//header//div[contains(@class, 'header__logo')]")  # Логотип Stellar Burgers
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка оформления заказа после входа
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")  # Заголовок конструктора

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::*")  # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::*")  # Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::*")  # Вкладка «Начинки»


class AuthLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")  # Заголовок формы входа
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/parent::*//input")  # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::*//input")  # Поле «Пароль»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа в форме
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» в формах регистрации/восстановления
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка восстановления пароля


class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/parent::*//input")  # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/parent::*//input")  # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::*//input")  # Поле «Пароль»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    PASSWORD_ERROR = (
        By.XPATH,
        "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]",
    )  # Ошибка при пароле короче 6 символов


class AccountLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход' or text()='Выйти']")  # Кнопка выхода из аккаунта
