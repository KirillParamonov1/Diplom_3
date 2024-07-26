from selenium.webdriver.common.by import By


class LoginPageLocators:
    NEW_PASSWORD = (By.XPATH, ".//a[text() = 'Восстановить пароль']") # Кнопка "Восстановить пароль"
    NEW_PASSWORD_HEADER = (By.XPATH, './/h2[text()="Восстановление пароля"]') # Заголовок "Восстановление пароля" на странице восстановления пароля