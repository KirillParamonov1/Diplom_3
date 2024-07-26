from pages.base_page import BasePage
import allure


class TestBasePage:

    @allure.title("Проверка клика по кнопке 'Личный кабинет'")
    def test_click_on_cabinet_button(self, driver):
        base_page = BasePage(driver)
        base_page.click_on_cabinet_button_in_the_general()
        new_url = base_page.get_url_for_page_for_test

        assert '/login' in new_url