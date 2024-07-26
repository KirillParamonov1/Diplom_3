from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_ORDER = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]') # Первый заказ в истории заказов пользователя
    ORDER_INFORMATION_WINDOW = (By.XPATH, './/div[contains(@class, "Modal_orderBox__1xWdi")]/parent::div/parent::section') # Окно с информацией о заказе
    EMAIL_AUTHORIZATION_SELECTOR = (By.XPATH,".//input[@class = 'text input__textfield text_type_main-default' and  @name = 'name']")  # Поле ввода email в форме авторизации на сайте
    PASSWORD_AUTHORIZATION_SELECTOR = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля в форме авторизации на сайте
    AUTHORIZATION_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка "Войти" на странице авторизации на сайте
    INGREDIENT_BUN_FIRST = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]") # Первый ингредиент в конструкторе ингредиентов
    INGREDIENT_CONTAINER = (By.XPATH, ".//div[@class = 'constructor-element constructor-element_pos_top']") # "Корзина" для перемещения ингредиентов и создания заказа
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']") # Кнопка "Оформить заказ" на главной странице сайта
    EXIT_WINDOW_ORDER_INFORMATION = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # Кнопка закрытия окна с информацией о заказе
    FIRST_ORDER_OF_ORDER_LIST = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]') # Первый заказ в ленте заказов
    ORDER_NUMBER_IN_WINDOW = (By.XPATH, './/p[contains(@class, "text text_type_digits-default mb-10 mt-5")]') # Номер первого заказа в ленте заказов в открытом всплывающем окне
    ORDER_NUMBER_FROM_INFORMATION_WINDOW = (By.XPATH, './/h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]') # Номер заказа во всплывающем окне после оформления заказа
    ALL_COUNT_ORDERS = (By.XPATH, '(.//p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"])[1]') # Счетчик всех заказов
    DAY_COUNT_ORDERS = (By.XPATH, '(.//p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"])[2]') # Счетчик заказов за день
    NOW_ORDER = (By.XPATH, '(.//li[@class = "text text_type_digits-default mb-2"])[6]') # Номер заказа "В работе"
    LAST_ORDER_IN_ORDERS_HISTORY = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[last()]') # Последний заказ в истории заказов пользователя
    NUMBER_OF_LAST_ORDER_IN_ORDERS_HISTORY = (By.XPATH, '(.//p[@class = "text text_type_digits-default"])[last()]') # Номер последнего заказа в истории заказов пользователя
    NUMBER_OF_FIRST_ORDER_IN_ORDER_LIST = (By.XPATH, '(.//p[@class = "text text_type_digits-default"])[1]') # Номер самого верхнего заказа в листе заказов
    STANDART_ORDER_ID = (By.XPATH, "//h2[text()='9999']") # Исчезающий номер заказа во всплывающем окне после оформления заказа