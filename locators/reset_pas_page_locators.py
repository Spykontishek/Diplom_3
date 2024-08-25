from selenium.webdriver.common.by import By


class Locators:
    SHOW_HIDE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon svg path")
    ACTIVE_FIELD_PASSWORD = (By.XPATH, "//label[contains(@class, 'input__placeholder-focused')]")