import allure
from conftest import driver
from pages.main_page import MainPage
from constants import Constants

class TestConstructorButton:
    @allure.title('Проверка кнопки "Конструктор"')
    @allure.description('Нажатие на кнопку и проверка, что кнопка ведет на главную страницу сайта')
    def test_click_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        current_url = driver.current_url
        assert current_url == Constants.URL