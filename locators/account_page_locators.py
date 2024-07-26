from selenium.webdriver.common.by import By


class AccountPageLocators:
    EMAIL_AUTHORIZATION_SELECTOR = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and  @name = 'name']")  # Поле ввода email в форме авторизации на сайте
    PASSWORD_AUTHORIZATION_SELECTOR = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля в форме авторизации на сайте
    AUTHORIZATION_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка "Войти" на странице авторизации на сайте
    CREATE_BURGER_HEADER = (By.XPATH, ".//h1[text() = 'Соберите бургер']") #Кнопка "Собери бургер" на главной странице
    CABINET_BUTTON = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Кнопка "Личный кабинет" в верхней части сайта
    PROFILE = (By.XPATH, ".//a[text() = 'Профиль']") # Кнопка "Профиль" на странице с личными данными пользователя
    ORDERS_HISTORY = (By.XPATH, ".//a[text() = 'История заказов']") # Кнопка "История заказов" на странице с личными данными пользователя
    EXIT = (By.XPATH, ".//button[text() = 'Выход']") # Кнопка "Выход" на странице с личными данными пользователя
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']") # Кнопка "Оформить заказ" на главной странице сайта
    ORDER_INFORMATION = (By.XPATH, ".//p[text() = 'Ваш заказ начали готовить']") # Статус заказа во всплывающем окне после оформления заказа