import allure
from locators.personal_account_page_locators import Locators
from pages.base_page import BasePage
from data import Data

class PersAcPage(BasePage):

    @allure.step('клик по кнопке "История заказов"')
    def click_order_history_button(self):
        self.click_method(Locators.ORDER_HISTORY_BUTTON)

    @allure.step('клик по кнопке "История заказов" с помощью Java')
    def click_order_history_button_java(self):
        self.click_java_method(Locators.ORDER_HISTORY_BUTTON)

    @allure.step('Ожидание перехода на страницу истории заказов')
    def wait_go_to_order_history_url(self):
        self.wait_url_to_be_visible_method(Data.ORDER_HISTORY_URL)

    @allure.step('клик по кнопке "Выход"')
    def click_exit_button(self):
        self.click_method(Locators.EXIT_BUTTON)

    @allure.step('Ожидание перехода на страницу авторизации')
    def wait_go_to_auth_url(self):
        self.wait_url_to_be_visible_method(Data.AUTH_URL)

    @allure.step('Ожидание пока кнопка "История заказов" станет кликабельна')
    def wait_order_history_button_is_clickable(self):
        self.wait_element_to_be_clickable_method(Locators.ORDER_HISTORY_BUTTON)
