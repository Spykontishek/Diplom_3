from selenium.webdriver.common.by import By


class ResetPasPage:
    SHOW_HIDE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon svg path")
    ACTIVE_FIELD_PASSWORD = (By.XPATH, "//label[contains(@class, 'input__placeholder-focused')]")

    def __init__(self, driver):
        self.driver = driver

    def click_show_hide_password_button(self):
        self.driver.find_element(*self.SHOW_HIDE_PASSWORD_BUTTON).click()


