from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants


class ForgotPasPage:
    EMAIL_FIELD = (By.XPATH, "//input[@class = 'text input__textfield text_type_main-default']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def click_restore_button(self):
        self.driver.find_element(*self.RESTORE_BUTTON).click()

    def wait_go_to_reset_pas_url(self):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Constants.RESET_PAS_URL))