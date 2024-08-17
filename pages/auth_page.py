from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants


class AuthPage:
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")

    def __init__(self, driver):
        self.driver = driver

    def click_restore_password_button(self):
        self.driver.find_element(*self.RESTORE_PASSWORD_BUTTON).click()

    def wait_go_to_forgot_pas_url(self):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Constants.FORGOT_PAS_URL))


