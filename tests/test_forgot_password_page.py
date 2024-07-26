from pages.forgot_password_page import ForgotPasswordPage
import allure


class TestForgotPasswordPage:

    @allure.title("Проверка перехода на страницу восстановления пароля после ввода email и клика на кнопку 'Восстановить'")
    def test_send_email_for_reset(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.email_input()
        forgot_password_page.click_on_button_reset()
        forgot_password_page.wait_for_input_code()
        reset_url = forgot_password_page.get_url_for_page_for_test

        assert '/reset-password' in reset_url

    @allure.title("Проверка того, что поле с паролем активно при нажатии на иконку глаза")
    def test_password_show(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.email_input()
        forgot_password_page.click_on_button_reset()
        forgot_password_page.wait_for_input_code()
        forgot_password_page.new_password_input()
        forgot_password_page.click_on_eye_password()

        assert forgot_password_page.find_active_eye()