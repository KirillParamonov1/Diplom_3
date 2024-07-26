from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.account_page_locators import AccountPageLocators
import data
import allure


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Авторизация на сайте под данными тестового пользователя")
    def authorization(self):
        self.driver.get(data.MAIN_URL + data.LOGIN_URL)
        self.set_text_to_element(AccountPageLocators.EMAIL_AUTHORIZATION_SELECTOR, data.TEST_USER_EMAIL)
        self.set_text_to_element(AccountPageLocators.PASSWORD_AUTHORIZATION_SELECTOR, data.TEST_USER_PASSWORD)
        self.click_on_element(AccountPageLocators.AUTHORIZATION_BUTTON)
        self.click_on_element(AccountPageLocators.AUTHORIZATION_BUTTON)
        self.find_element_with_wait(AccountPageLocators.CREATE_BURGER_HEADER)
        self.click_on_element(AccountPageLocators.CABINET_BUTTON)
        self.find_elements(AccountPageLocators.PROFILE)

    @allure.step("Клик по кнопке 'История заказов' в профиле авторизованного пользователя")
    def click_on_orders_history(self):
        self.click_on_element(AccountPageLocators.ORDERS_HISTORY)

    @allure.step("Клик по кнопке 'Выйти' в профиле авторизованного пользователя")
    def click_on_exit_button(self):
        self.click_on_element(AccountPageLocators.EXIT)

    @allure.step("Ожидание появления кнопки 'Войти' на странице авторизации")
    def wait_for_authorization_button(self):
        self.find_element_with_wait(AccountPageLocators.AUTHORIZATION_BUTTON)

    @allure.step("Создание заказа под авторизованным пользователем")
    def create_order(self):
        self.driver.get(data.MAIN_URL + data.LOGIN_URL)
        self.set_text_to_element(AccountPageLocators.EMAIL_AUTHORIZATION_SELECTOR, data.TEST_USER_EMAIL)
        self.set_text_to_element(AccountPageLocators.PASSWORD_AUTHORIZATION_SELECTOR, data.TEST_USER_PASSWORD)
        self.click_on_element(AccountPageLocators.AUTHORIZATION_BUTTON)
        self.click_on_element(AccountPageLocators.AUTHORIZATION_BUTTON)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN_FIRST, MainPageLocators.INGREDIENT_CONTAINER)

    @allure.step("Клик по кнопке 'Сделать заказ'")
    def click_on_button_order(self):
        self.click_on_element(AccountPageLocators.ORDER_BUTTON)

    @allure.step("Ожидание статуса заказа во всплывающем окне после оформления заказа")
    def wait_for_order_information(self):
        return self.find_element_with_wait(AccountPageLocators.ORDER_INFORMATION)