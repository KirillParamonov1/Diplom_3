from pages.login_page import LoginPage
import allure


class TestLoginPage:

    @allure.title("Проверка клика на кнопку 'Забыли пароль' и перехода на страницу восстановления пароля")
    def test_click_on_new_password(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.click_on_new_password_button()
        password_url = login_page.get_url_for_page_for_test

        assert 'forgot-password' in password_url