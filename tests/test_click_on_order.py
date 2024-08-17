import allure
from pages.order_feed_page import OrderFeedPage
from constants import Constants
from locators.order_feed_page_locators import Locators
from conftest import driver, reg, log, create_order

class TestClickOnOrder:
    @allure.title('Проверка нажатия на заказ')
    @allure.description('Нажатие на заказ и проверка, что появилось всплывающее окно с деталями заказа')
    def test_click_on_order(self, driver, create_order):
        driver.get(Constants.ORDER_FEED_URL)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_any_order_to_be_visible()
        order_feed_page.click_on_order()
        order_feed_page.wait_order_pop_up_window_is_displayed()
        assert driver.find_element(*Locators.ORDER_FEED_POP_UP_OF_ORDER).is_displayed()