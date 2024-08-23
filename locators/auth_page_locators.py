from selenium.webdriver.common.by import By


class LocatorsAuth:
    EMAIL_FIELD = (By.XPATH, "//input[contains(@name, 'name')]")
    PASSWORD_FIELD = (By.XPATH, "//input[contains(@name, 'Пароль')]")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")