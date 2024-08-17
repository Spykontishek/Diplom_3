import allure
from conftest import driver
from pages.main_page import MainPage
from locators.main_page_locators import Locators

class TestClickOnIngredient:
    @allure.title('Проверка нажатия на ингридиент')
    @allure.description('Нажатие на ингридиент и проверка, что появилось всплывающее окно с деталями')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_ingredient_pop_up_window_is_displayed()
        assert driver.find_element(*Locators.INGREDIENT_POP_UP_WINDOW).is_displayed()