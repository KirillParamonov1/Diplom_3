import allure
import pytest
from selenium import webdriver

import data


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
@allure.title('Запуск драйвера')
def driver(request):
    if 'chrome' in request.param:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif 'firefox' in request.param:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')

        driver = webdriver.Firefox(options=options)

    driver.get(data.MAIN_URL)

    yield driver

    driver.quit()