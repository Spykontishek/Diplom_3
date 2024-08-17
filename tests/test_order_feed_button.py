import allure
from conftest import driver
from pages.main_page import MainPage
from constants import Constants

class TestOrderFeedButton:
    @allure.title('Проверка кнопки "Лента Заказов"')
    @allure.description('Нажатие на кнопку и проверка, что кнопка ведет на страницу заказов')
    def test_click_order_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        main_page.wait_go_to_order_feed_url()
        current_url = driver.current_url
        assert current_url == Constants.ORDER_FEED_URL