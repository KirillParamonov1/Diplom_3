from selenium.webdriver.common.by import By


class BasePageLocators:
    CABINET_BUTTON_IN_GENERAL = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Кнопка "Личный Кабинет" в правом верхнем углу сайта
    NEW_PASSWORD_HEADER = (By.XPATH, './/h2[text()="Восстановление пароля"]') # Кнопка "Восстановление пароля" на странице авторизации
    WELCOME_BUTTON = (By.XPATH, './/button[text()="Войти"]') # Кнопка "Войти" на странице авторизации