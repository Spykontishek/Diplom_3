from locators.forgot_pas_page_locators import Locators
import allure
from pages.base_page import BasePage
from data import Data

class ForgotPasPage(BasePage):
    @allure.step('Заполнение поля "Email"')
    def set_email(self, email):
        self.send_keys_method(Locators.EMAIL_FIELD, email)

    @allure.step('клик по кнопке "Восстановить"')
    def click_restore_button(self):
        self.click_method(Locators.RESTORE_BUTTON)

    @allure.step('Ожидания перехода на 2-ую страницу восстановления пароля')
    def wait_go_to_reset_pas_url(self):
        self.wait_url_to_be_visible_method(Data.RESET_PAS_URL)

    @allure.step('Переход на 1-ую страницу восстановления пароля')
    def navigate_forgot_pas_url(self):
        self.navigate_url_method(Data.FORGOT_PAS_URL)