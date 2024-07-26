from pages.order_page import OrderPage
import allure


class TestOrderPage:

    @allure.title("Проверка открытия вспылвающего окна с деталями заказа при клике на заказ в ленте заказов")
    def test_open_window_with_information_about_order(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        order_page.click_on_order()

        assert order_page.find_order_information_window()

    @allure.title("Проверка, что номер заказа пользователя из истории заказов есть в листе заказов")
    def test_put_user_order_to_order_list(self, driver):
        order_page = OrderPage(driver)
        order_page.create_order()
        number_of_user_order = order_page.search_number_of_order()
        number_in_number_list = order_page.number_of_last_order_in_order_list_from_order_history()

        assert number_of_user_order == number_in_number_list

    @allure.title("Проверка, что после создания заказа счетчик всех выполненных заказов увеличивается")
    def test_count_of_all_orders(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        befor_order = order_page.return_count_of_all_orders()
        order_page.create_order()
        order_page.number_of_last_user_order()
        order_page.go_to_order_page()
        after_order = order_page.return_count_of_all_orders()

        assert int(after_order) > int(befor_order)

    @allure.title("Проверка, что после создания заказа счетчик выполненных за день заказов увеличивается")
    def test_count_of_day_orders(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        befor_order = order_page.return_count_of_day_orders()
        order_page.create_order()
        order_page.go_to_order_page()
        after_order = order_page.return_count_of_day_orders()

        assert int(after_order) > int(befor_order)

    @allure.title("Проверка, что номер только что созданного заказа появляется в разделе 'В работе' в листе заказов")
    def test_count_now_order(self, driver):
        order_page = OrderPage(driver)
        order_page.create_order()
        order_number = order_page.return_order_id()
        order_page.go_to_order_page()
        order_number_in_order_list = order_page.return_now_order()

        assert order_number in order_number_in_order_list