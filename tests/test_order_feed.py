import allure
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.personal_account_page import PersAcPage
from pages.order_history_page import OrderHistoryPage
from conftest import driver, reg, log, create_order

class TestOrderFeed:
    @allure.title('Проверка нажатия на заказ')
    @allure.description('Нажатие на заказ и проверка, что появилось всплывающее окно с деталями заказа')
    def test_click_on_order(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate_order_feed_url()
        order_feed_page.wait_for_any_order_to_be_visible()
        order_feed_page.click_on_order()
        order_feed_page.wait_order_pop_up_window_is_visible()
        assert order_feed_page.pop_up_is_displayed() is True

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
        main_page.click_constructor_button()
        order_feed_page = OrderFeedPage(driver)
        main_page.wait_order_feed_button_to_be_clickable()
        main_page.click_order_feed_button_java()
        main_page.wait_go_to_order_feed_url()
        order_feed_page.wait_for_orders_to_be_visible()
        all_orders_texts = order_feed_page.get_all_orders_texts()
        assert any(number_of_order in order_text for order_text in all_orders_texts)

    @allure.title('Проверка счетчика заказов выполненных за все время')
    @allure.description('Сравнение, что после созданного заказа, счетчик увеличился')
    def test_counter_orders_for_all_time(self, driver, log):
        main_page = MainPage(driver)
        main_page.wait_order_feed_button_to_be_clickable()
        main_page.click_order_feed_button()
        main_page.wait_go_to_order_feed_url()
        order_feed_page = OrderFeedPage(driver)
        text_1 = order_feed_page.get_number_of_orders_for_all_time()
        main_page.navigate_main_url()
        main_page.wait_for_any_bun_to_be_visible()
        main_page.move_bun_to_burger_constructor()
        main_page.click_on_place_an_order_button()
        main_page.wait_order_pop_up_window_is_visible()
        main_page.click_on_x_button_java()
        main_page.wait_pop_up_window_is_not_displayed()
        main_page.click_order_feed_button_java()
        text_2 = order_feed_page.get_number_of_orders_for_all_time()
        assert text_2 > text_1

    @allure.title('Проверка счетчика заказов выполненных за сегодня')
    @allure.description('Сравнение, что после созданного заказа, счетчик увеличился')
    def test_counter_orders_for_today(self, driver, log):
        main_page = MainPage(driver)
        main_page.wait_order_feed_button_to_be_clickable()
        main_page.click_order_feed_button()
        main_page.wait_go_to_order_feed_url()
        order_feed_page = OrderFeedPage(driver)
        text_1 = order_feed_page.get_number_of_orders_for_today()
        main_page.navigate_main_url()
        main_page.wait_for_any_bun_to_be_visible()
        main_page.move_bun_to_burger_constructor()
        main_page.click_on_place_an_order_button()
        main_page.wait_order_pop_up_window_is_visible()
        main_page.click_on_x_button_java()
        main_page.wait_pop_up_window_is_not_displayed()
        main_page.click_order_feed_button_java()
        text_2 = order_feed_page.get_number_of_orders_for_today()
        assert text_2 > text_1

    @allure.title('Проверка отображения заказов "В работе"')
    @allure.description('Создание заказа и проверка что его номер заказа присутствует "В работе"')
    def test_appearance_orders_in_progress(self, driver, create_order):
        main_page = MainPage(driver)
        main_page.personal_account_button_is_clickable()
        main_page.click_personal_account_button_java()
        main_page.wait_go_to_personal_account_url()
        pers_ac_page = PersAcPage(driver)
        pers_ac_page.wait_order_history_button_is_clickable()
        pers_ac_page.click_order_history_button_java()
        pers_ac_page.wait_go_to_order_history_url()
        order_history_page = OrderHistoryPage(driver)
        number_of_order = order_history_page.get_number_of_order()[1:]
        main_page.click_constructor_button()
        main_page.wait_order_feed_button_to_be_clickable()
        main_page.click_order_feed_button_java()
        main_page.wait_go_to_order_feed_url()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_orders_in_progress_to_be_visible()
        all_orders_in_progress_texts = order_feed_page.get_all_orders_in_progress_texts()
        assert any(number_of_order in order_text for order_text in all_orders_in_progress_texts)
