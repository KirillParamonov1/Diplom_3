from pages.account_page import AccountPage
import allure


class TestAccountPage:

    @allure.title("Проверка клика по кнопке 'История заказов'")
    def test_click_on_order_history(self, driver):
        account_page = AccountPage(driver)
        account_page.authorization()
        account_page.click_on_orders_history()
        new_url = account_page.get_url_for_page_for_test

        assert '/order-history' in new_url

    @allure.title("Проверка клика по кнопке 'Выйти'")
    def test_click_on_exit(self, driver):
        account_page = AccountPage(driver)
        account_page.authorization()
        account_page.click_on_exit_button()
        account_page.wait_for_authorization_button()
        new_url = account_page.get_url_for_page_for_test

        assert '/login' in new_url

    @allure.title("Проверка создания заказа под авторизованным пользователем")
    def test_create_order_for_login_user(self, driver):
        account_page = AccountPage(driver)
        account_page.create_order()
        account_page.click_on_button_order()

        assert account_page.wait_for_order_information()