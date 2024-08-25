import allure
from conftest import driver, reg, log
from pages.main_page import MainPage
from data import Data

class TestMainFunctionality:
    @allure.title('Проверка кнопки "Конструктор"')
    @allure.description('Нажатие на кнопку и проверка, что кнопка ведет на главную страницу сайта')
    def test_click_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        current_url = main_page.get_current_url_method()
        assert current_url == Data.URL

    @allure.title('Проверка кнопки "Лента Заказов"')
    @allure.description('Нажатие на кнопку и проверка, что кнопка ведет на страницу заказов')
    def test_click_order_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        main_page.wait_go_to_order_feed_url()
        current_url = main_page.get_current_url_method()
        assert current_url == Data.ORDER_FEED_URL

    @allure.title('Проверка нажатия на ингридиент')
    @allure.description('Нажатие на ингридиент и проверка, что появилось всплывающее окно с деталями')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_order_pop_up_window_is_visible()
        assert main_page.pop_up_is_displayed() is True

    @allure.title('Проверка нажатия на крестик всплывающего окна')
    @allure.description('Нажатие на крестик и проверка, что окно закрылось')
    def test_click_on_x_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_ingredient_pop_up_window_is_displayed()
        main_page.click_x_button()
        assert main_page.wait_ingredient_pop_up_window_is_not_visible() is True

    @allure.title('Проверка счетчика ингридиента')
    @allure.description('Добавление  ингридиента в заказ и проверка, что счетчик ингридиента увеличился')
    def test_counter_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.move_ingredient_to_burger_constructor()
        main_page.counter_of_ingredient_is_visible()
        assert main_page.counter_of_ingredient_is_displayed() is True

    @allure.title('Проверка создания заказа')
    @allure.description('оформление заказа и проверка что появилось всплывающее окно с деталями заказа')
    def test_create_order(self,driver, log):
        main_page = MainPage(driver)
        main_page.wait_for_any_bun_to_be_visible()
        main_page.move_bun_to_burger_constructor()
        main_page.click_on_place_an_order_button()
        main_page.wait_order_pop_up_window_is_visible()
        assert main_page.pop_up_is_displayed() is True