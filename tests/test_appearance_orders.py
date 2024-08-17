import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersAcPage
from pages.order_history_page import OrderHistoryPage
from pages.order_feed_page import OrderFeedPage
from constants import Constants
from conftest import driver, reg, log, create_order

class TestAppearanceOrders:
    ORDER_CONFIRMATION_WINDOW = OrderHistoryPage.ORDER_CONFIRMATION_WINDOW
    @allure.title('Проверка отображения заказов пользователя')
    @allure.description('Переход в раздел "История заказов" и проверка что все заказы оттуда отображаются и в "Ленте заказов"')
    def test_appearance_orders(self, driver, create_order):
        main_page = MainPage(driver)
        main_page.personal_account_button_is_clickable()
        main_page.click_personal_account_button_java()
        main_page.wait_go_to_personal_account_url()
        pers_ac_page = PersAcPage(driver)
        pers_ac_page.wait_order_history_button_is_clickable()
        pers_ac_page.click_order_history_button_java()
        pers_ac_page.wait_go_to_order_history_url()
        order_history_page = OrderHistoryPage(driver)
        number_of_order = order_history_page.get_number_of_order()
        driver.get(Constants.URL)
        main_page.wait_order_feed_button_to_be_clickable()
        main_page.click_order_feed_button_java()
        main_page.wait_go_to_order_feed_url()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_orders_to_be_visible()
        all_orders_texts = order_feed_page.get_all_orders_texts()
        assert any(number_of_order in order_text for order_text in all_orders_texts)