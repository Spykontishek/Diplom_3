from locators.order_feed_page_locators import Locators
import allure
from pages.base_page import BasePage
from data import Data
class OrderFeedPage(BasePage):


    @allure.step('ожидание пока информация о сделанных заказах станет видимой')
    def wait_for_any_order_to_be_visible(self):
        self.wait_element_to_be_visible_method(Locators.ANY_ORDER)

    @allure.step('клик по 1-ому из заказов')
    def click_on_order(self):
        self.click_method(Locators.ANY_ORDER)

    @allure.step('ожидание пока всплывающее окно с информацией о заказе станет видимой')
    def wait_order_pop_up_window_is_visible(self):
        self.wait_element_to_be_visible_method(Locators.ORDER_FEED_POP_UP_OF_ORDER)

    @allure.step('проверка, что всплывающее окно открылось')
    def pop_up_is_displayed(self):
        self.element_is_displayed_method(Locators.ORDER_FEED_POP_UP_OF_ORDER)
    @allure.step('получение текста из всех заказов на странице')
    def get_all_orders_texts(self):
        return self.get_all_elements_texts_method(Locators.ORDERS_LIST)
    @allure.step('ожидание пока заказы станут видимыми')
    def wait_for_orders_to_be_visible(self):
        self.wait_all_elements_to_be_visible_method(Locators.ORDERS_LIST)
    @allure.step('ожидание пока текст с заказами "Выполнено за все время:" станет видимый и получение числа заказов из него ')
    def get_number_of_orders_for_all_time(self):
        self.wait_element_to_be_visible_method(Locators.TOTAL_COMPLETED_ORDERS_COUNTER)
        return self.get_element_text_method(Locators.TOTAL_COMPLETED_ORDERS_COUNTER)
    @allure.step('ожидание пока текст с заказами "Выполнено за сегодня:" станет видимый и получение числа заказов из него ')
    def get_number_of_orders_for_today(self):
        self.wait_element_to_be_visible_method(Locators.COMPLETED_ORDERS_FOR_TODAY_COUNTER)
        return self.get_element_text_method(Locators.COMPLETED_ORDERS_FOR_TODAY_COUNTER)
    @allure.step('ожидание пока заказы находящиеся "В работе:" станут видимыми')
    def wait_for_orders_in_progress_to_be_visible(self):
        self.wait_all_elements_to_be_visible_method(Locators.ORDERS_IN_PROGRESS_LIST)
    @allure.step('получение текста из всех заказов "В работе:"')
    def get_all_orders_in_progress_texts(self):
        return self.get_all_elements_texts_method(Locators.ORDERS_IN_PROGRESS_LIST)

    @allure.step('Ожидания перехода на страницу личного кабинета')
    def wait_go_to_test(self):
        self.wait_url_to_be_visible_method(Data.URL)

    @allure.step('Переход на страницу ленты заказов')
    def navigate_order_feed_url(self):
        self.navigate_url_method(Data.ORDER_FEED_URL)
