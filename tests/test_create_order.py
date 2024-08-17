import allure
from conftest import driver, reg, log
from pages.main_page import MainPage
from locators.main_page_locators import Locators

class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('оформление заказа и проверка что появилось всплывающее окно с деталями заказа')
    def test_create_order(self,driver, log):
        main_page = MainPage(driver)
        main_page.wait_for_any_bun_to_be_visible()
        main_page.move_bun_to_burger_constructor()
        main_page.click_on_place_an_order_button()
        main_page.wait_order_pop_up_window_is_displayed()
        assert driver.find_element(*Locators.ORDER_POP_UP_WINDOW).is_displayed()