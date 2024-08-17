import allure
from conftest import driver
from pages.main_page import MainPage


class TestClickOnXButton:
    @allure.title('Проверка нажатия на крестик всплывающего окна')
    @allure.description('Нажатие на крестик и проверка, что окно закрылось')
    def test_click_on_x_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_ingredient_pop_up_window_is_displayed()
        main_page.click_x_button()
        assert main_page.wait_pop_up_window_is_not_displayed() == True