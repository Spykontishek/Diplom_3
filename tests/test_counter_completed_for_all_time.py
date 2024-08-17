import allure
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.order_feed_page import OrderFeedPage
from constants import Constants
from conftest import driver, reg, log

class TestCounterOrdersForAllTime:
    ORDER_CONFIRMATION_WINDOW = OrderHistoryPage.ORDER_CONFIRMATION_WINDOW
    @allure.title('Проверка счетчика заказов выполненных за все время')
    @allure.description('Сравнение, что после созданного заказа, счетчик увеличился')
    def test_counter_orders_for_all_time(self, driver, log):
        main_page = MainPage(driver)
        main_page.wait_order_feed_button_to_be_clickable()
        main_page.click_order_feed_button()
        main_page.wait_go_to_order_feed_url()
        order_feed_page = OrderFeedPage(driver)
        text_1 = order_feed_page.get_number_of_orders_for_all_time()
        driver.get(Constants.FORGOT_PAS_URL)
        main_page.wait_for_any_bun_to_be_visible()
        main_page.move_bun_to_burger_constructor()
        main_page.click_on_place_an_order_button()
        main_page.wait_order_pop_up_window_is_displayed()
        main_page.click_on_x_button_java()
        main_page.wait_pop_up_window_is_not_displayed()
        main_page.click_order_feed_button_java()
        text_2 = order_feed_page.get_number_of_orders_for_all_time()
        assert text_2 > text_1

