import allure
from locators.reset_pas_page_locators import Locators
from pages.base_page import BasePage

class ResetPasPage(BasePage):

    @allure.step('Клик по кнопке "показать/скрыть пароль')
    def click_show_hide_password_button(self):
        self.click_method(Locators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step('проверка, что поле "Пароль" подсветилось')
    def active_field_password_is_displayed(self):
        self.element_is_displayed_method(Locators.ACTIVE_FIELD_PASSWORD)


