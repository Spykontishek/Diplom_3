from locators.order_history_page_locators import Locators
import allure
from pages.base_page import BasePage
class OrderHistoryPage(BasePage):

    @allure.step('ожидание пока информация о сделанном заказе станет видима и возвращение текста номера этого заказа')
    def get_number_of_order(self):
        self.wait_element_to_be_visible_method(Locators.ORDER_CONFIRMATION_WINDOW)
        return self.get_element_text_method(Locators.ORDER_CONFIRMATION_WINDOW)




