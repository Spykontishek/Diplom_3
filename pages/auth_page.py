import allure
from locators.auth_page_locators import LocatorsAuth
from pages.base_page import BasePage
from data import Data

class AuthPage(BasePage):


    @allure.step('клик по кнопке "Восстановить пароль"')
    def click_restore_password_button(self):
        self.click_method(LocatorsAuth.RESTORE_PASSWORD_BUTTON)

    @allure.step('Ожидания перехода на 1-ую страницу восстановления пароля')
    def wait_go_to_forgot_pas_url(self):
        self.wait_url_to_be_visible_method(Data.FORGOT_PAS_URL)

    @allure.step('Переход на страницу авторизации')
    def navigate_auth_url(self):
        self.navigate_url_method(Data.AUTH_URL)

