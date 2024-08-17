import allure
from conftest import driver, reg, log
from pages.main_page import MainPage
from constants import Constants

class TestPersonalAccountButton:
    @allure.title('Проверка кнопки "Личный Кабинет"')
    @allure.description('Нажатие на кнопку и проверка, что осуществился переход на страницу личного кабинета')
    def test_click_personal_account_button(self,driver, log):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.wait_go_to_personal_account_url()
        current_url = driver.current_url
        assert current_url == Constants.PERSONAL_ACC_URL