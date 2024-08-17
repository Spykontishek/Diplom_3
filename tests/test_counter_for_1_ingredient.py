import allure
from conftest import driver
from pages.main_page import MainPage
from locators.main_page_locators import Locators

class TestCounterOfIngredient:
    @allure.title('Проверка счетчика ингридиента')
    @allure.description('Добавление  ингридиента в заказ и проверка, что счетчик ингридиента увеличился')
    def test_counter_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.move_ingredient_to_burger_constructor()
        assert driver.find_element(*Locators.COUNTER_OF_INGREDIENT).is_displayed()