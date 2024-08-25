from selenium.webdriver.common.by import By


class Locators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    ANY_INGREDIENT = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']")
    INGREDIENT_POP_UP_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_modal__contentBox')]")
    X_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close_modified')]")
    COUNTER_OF_INGREDIENT = (By.XPATH, "//p[contains(@class, 'counter_counter__num') and text()='1']")
    BURGER_CONSTRUCTOR = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    ANY_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_POP_UP_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
