from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default']") # Поле ввода email на странице восстановления пародя
    BUTTON_RESET = (By.XPATH, './/button[text() = "Восстановить"]') # Кнопка "Восстановить" на странице восстановления пароля
    INPUT_CODE = (By.XPATH, './/label[text() = "Введите код из письма"]') # Поле ввода кода из письма на странице восстановления пароля
    INPUT_PASSWORD = (By.XPATH, './/input[@type = "password"]') # Поле ввода пароля на странице восстановления пароля
    EYE_PASSWORD = (By.XPATH, './/div[@class = "input__icon input__icon-action"]') # Иконка глаза на странице восстановления пароля
    SHOW_EYE_PASSWORD = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']") # Иконка глаза, когда он активен и пароль показан