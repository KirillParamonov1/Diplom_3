from pages.base_page import BasePage
import data
from locators.forgot_password_locators import ForgotPasswordLocators
import allure


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_forgot_password_page(self):
        self.driver.get(data.MAIN_URL+data.FORGOT_PASSWORD_URL)

    @allure.step("Ввод email  форме восстановления пароля")
    def email_input(self):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, data.TEST_USER_EMAIL)

    @allure.step("Ввод нового пароля в поле восстановления пароля")
    def new_password_input(self):
        self.set_text_to_element(ForgotPasswordLocators.INPUT_PASSWORD, data.TEST_USER_NEW_PASSWORD)

    @allure.step("Нажатие на кнопку 'Восстановить'")
    def click_on_button_reset(self):
        self.click_on_element(ForgotPasswordLocators.BUTTON_RESET)

    @allure.step("Ожидание появления поля 'Введите код из письма'")
    def wait_for_input_code(self):
        self.find_element_with_wait(ForgotPasswordLocators.INPUT_CODE)

    @allure.step("Клик по иконке с глазом")
    def click_on_eye_password(self):
        self.click_on_element(ForgotPasswordLocators.EYE_PASSWORD)

    @allure.step("Поиск 'активного глаза'")
    def find_active_eye(self):
        return self.find_element_with_wait(ForgotPasswordLocators.SHOW_EYE_PASSWORD)