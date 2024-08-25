from selenium.webdriver.common.by import By


class Locators:
    EMAIL_FIELD = (By.XPATH, "//input[@class = 'text input__textfield text_type_main-default']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")