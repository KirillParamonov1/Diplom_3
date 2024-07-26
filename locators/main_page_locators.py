from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR = (By.XPATH, ".//p[text() = 'Конструктор']") # Кнопка "Конструктор" на главной странице
    ORDERS_LIST = (By.XPATH, ".//p[text() = 'Лента Заказов']") # Кнопка "Лента Заказов" в верхней части сайта
    INGREDIENT_BUN_FIRST = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]") # Первый ингредиент в конструкторе ингредиентов
    INGREDIENT_WINDOW_HEADER = (By.XPATH, ".//h2[text() = 'Детали ингредиента']") # Заголовок всплывающего окна с информацией об ингредиенте
    INGREDIENT_WINDOW_EXIT = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # Кнопка выхода из всплывающего окна с информацией об ингредиенте
    INGREDIENT_CONTAINER = (By.XPATH, ".//div[@class = 'constructor-element constructor-element_pos_top']") # "Корзина" для перемещения ингредиентов и создания заказа
    INGREDIENT_COUNT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]") # Счетчик ингредиентов