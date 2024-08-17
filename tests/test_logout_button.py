import allure
from conftest import driver, reg, log
from pages.personal_account_page import PersAcPage
from pages.main_page import MainPage
from constants import Constants

class TestLogout:
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
        assert current_url == Constants.AUTH_URL