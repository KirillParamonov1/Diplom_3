from pages.main_page import MainPage
import allure
import data


class TestMainPage:

    @allure.title("Проверка клика по кнопке 'Конструктор' из личного кабинета")
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_cabinet_button_in_the_general()
        main_page.click_on_constructor_button()
        new_url = main_page.get_url_for_page_for_test

        assert new_url == data.MAIN_URL

    @allure.title("Проверка клика по кнопке 'Лист заказов'")
    def test_click_on_orders_list_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_orders_list_button()
        new_url = main_page.get_url_for_page_for_test

        assert '/feed' in new_url

    @allure.title("Проверка клика по ингредиенту и открытия всплывающего окна с информацией об ингредиенте")
    def test_click_on_ingredient_and_get_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()

        assert main_page.wait_for_ingredient_window()

    @allure.title("Проверка закрытия всплывающего окна с информацией об ингредиенте")
    def test_click_on_ingredient_window_exit(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.click_on_ingredient_window_exit()

        assert main_page.check_window_exit() is False

    @allure.title("Проверка увеличения количества ингредиентов на счетчике после добавления ингредиента в заказ")
    def test_ingredient_count(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()

        assert main_page.get_ingredient_counter() == '2'