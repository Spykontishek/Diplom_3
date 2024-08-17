import allure
from conftest import driver
from pages.auth_page import AuthPage
from constants import Constants

class TestRestorePasswordButton:
    @allure.title('Проверка кнопки "Восстановить пароль"')
    @allure.description('Нажатие на кнопку и проверка, что осуществился переход на страницу восстановления пароля')
    def test_click_restore_password_button(self, driver):
        driver.get(Constants.AUTH_URL)
        auth_page = AuthPage(driver)
        auth_page.click_restore_password_button()
        auth_page.wait_go_to_forgot_pas_url()
        current_url = driver.current_url
        assert current_url == Constants.FORGOT_PAS_URL