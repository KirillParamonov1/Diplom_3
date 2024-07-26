from pages.base_page import BasePage
import data
from locators.order_page_locators import OrderPageLocators
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по заказу")
    def click_on_order(self):
        self.click_on_element(OrderPageLocators.FIRST_ORDER)

    @allure.step("Поиск окна с информацией о заказе")
    def find_order_information_window(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_INFORMATION_WINDOW)

    @allure.step("Переход на страницу листа заказов")
    def go_to_order_page(self):
        self.driver.get(data.MAIN_URL+data.ORDER_URL)

    @allure.step("Ожидание статуса заказа во всплывающем окне после создания заказа")
    def wait_for_order_information(self):
        return self.find_element_with_wait(AccountPageLocators.ORDER_INFORMATION)

    @allure.step("Создание заказа")
    def create_order(self):
        self.driver.get(data.MAIN_URL+data.LOGIN_URL)
        self.set_text_to_element(OrderPageLocators.EMAIL_AUTHORIZATION_SELECTOR, data.TEST_USER_EMAIL)
        self.set_text_to_element(OrderPageLocators.PASSWORD_AUTHORIZATION_SELECTOR, data.TEST_USER_PASSWORD)
        self.click_on_element(OrderPageLocators.AUTHORIZATION_BUTTON)
        self.click_on_element(OrderPageLocators.AUTHORIZATION_BUTTON)
        self.drag_and_drop_element(OrderPageLocators.INGREDIENT_BUN_FIRST, OrderPageLocators.INGREDIENT_CONTAINER)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_order_information()

    @allure.step("Получение номера заказа из истории заказов пользователя")
    def search_number_of_order(self):
        self.wait_until_clickable(OrderPageLocators.EXIT_WINDOW_ORDER_INFORMATION)
        self.find_element_with_wait(OrderPageLocators.EXIT_WINDOW_ORDER_INFORMATION)
        self.click_on_element(OrderPageLocators.EXIT_WINDOW_ORDER_INFORMATION)
        self.wait_until_clickable(AccountPageLocators.CABINET_BUTTON)
        self.click_on_element(AccountPageLocators.CABINET_BUTTON)
        self.find_element_with_wait(AccountPageLocators.PROFILE)
        self.click_on_element(AccountPageLocators.ORDERS_HISTORY)
        self.find_element_with_wait(OrderPageLocators.FIRST_ORDER)
        self.scroll_to_element(OrderPageLocators.NUMBER_OF_LAST_ORDER_IN_ORDERS_HISTORY)
        return self.get_text_from_element(OrderPageLocators.NUMBER_OF_LAST_ORDER_IN_ORDERS_HISTORY)

    @allure.step("Получение id заказа")
    def return_order_id(self):
        self.wait_until_missing_element(OrderPageLocators.STANDART_ORDER_ID)
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_FROM_INFORMATION_WINDOW)

    @allure.step("Получение номера из последнего заказа в листе заказов")
    def number_of_last_order_in_order_list_from_order_history(self):
        self.go_to_order_page()
        self.click_on_element(MainPageLocators.ORDERS_LIST)
        return self.get_text_from_element(OrderPageLocators.NUMBER_OF_FIRST_ORDER_IN_ORDER_LIST)

    @allure.step("Получение номера заказа из окна информации о заказе")
    def number_of_last_user_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_FROM_INFORMATION_WINDOW)

    @allure.step("Получение количества всех выполненных заказов")
    def return_count_of_all_orders(self):
        return self.get_text_from_element(OrderPageLocators.ALL_COUNT_ORDERS)

    @allure.step("Получение количества всех заказов за день")
    def return_count_of_day_orders(self):
        return self.get_text_from_element(OrderPageLocators.DAY_COUNT_ORDERS)

    @allure.step("Получение значения заказа, который находится в работе")
    def return_now_order(self):
        self.find_element_with_wait(OrderPageLocators.NOW_ORDER)
        return self.get_text_from_element(OrderPageLocators.NOW_ORDER)