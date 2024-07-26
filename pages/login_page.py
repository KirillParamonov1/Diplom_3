import allure
import data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_on_new_password_button(self):
        self.click_on_element(LoginPageLocators.NEW_PASSWORD)

    @allure.step("Переход на страницу авторизации")
    def go_to_login_page(self):
        self.driver.get(data.MAIN_URL+data.LOGIN_URL)