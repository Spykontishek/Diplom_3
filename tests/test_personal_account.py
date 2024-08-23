import allure
from conftest import driver, reg, log
from pages.main_page import MainPage
from pages.personal_account_page import PersAcPage
from data import Data


class TestPersonalAccountButton:
    @allure.title('Проверка кнопки "Личный Кабинет"')
    @allure.description('Нажатие на кнопку и проверка, что осуществился переход на страницу личного кабинета')
    def test_click_personal_account_button(self,driver, log):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.wait_go_to_personal_account_url()
        current_url = driver.current_url
        assert current_url == Data.PERSONAL_ACC_URL

    @allure.title('Проверка кнопки "История заказов"')
    @allure.description('Нажатие на кнопку и проверка, что осуществился переход на страницу истории заказов')
    def test_click_order_history_button(self,driver, log):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.wait_go_to_personal_account_url()
        pers_ac_page = PersAcPage(driver)
        pers_ac_page.click_order_history_button()
        pers_ac_page.wait_go_to_order_history_url()
        current_url = driver.current_url
        assert current_url == Data.ORDER_HISTORY_URL

    @allure.title('Проверка выхода с аккаунта')
    @allure.description('Нажатие на кнопку "Выход"и проверка что осуществился переход на страницу аутентификации')
    def test_click_exit_button(self, driver, log):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.wait_go_to_personal_account_url()
        pers_ac_page = PersAcPage(driver)
        pers_ac_page.click_exit_button()
        pers_ac_page.wait_go_to_auth_url()
        current_url = driver.current_url
        assert current_url == Data.AUTH_URL