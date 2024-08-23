from selenium.webdriver.common.by import By


class Locators:
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, "//p[@class = 'text text_type_digits-default']")