from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR)

    @allure.step("Клик по кнопке 'Лист заказов'")
    def click_on_orders_list_button(self):
        self.click_on_element(MainPageLocators.ORDERS_LIST)

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_BUN_FIRST)

    @allure.step("Ожидание появления всплывающего окна с информацией об ингредиенте")
    def wait_for_ingredient_window(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_WINDOW_HEADER)

    @allure.step("Клик по кнопке закрытия всплывающего окна с ифнормацией об ингредиенте")
    def click_on_ingredient_window_exit(self):
        self.click_on_element(MainPageLocators.INGREDIENT_WINDOW_EXIT)

    @allure.step("Проверка, что всплывающее окно с информацией об ингредиенте закрыто")
    def check_window_exit(self):
        return self.element_exist(MainPageLocators.INGREDIENT_WINDOW_HEADER)

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN_FIRST, MainPageLocators.INGREDIENT_CONTAINER)

    @allure.step("Получение значения со счетчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNT)