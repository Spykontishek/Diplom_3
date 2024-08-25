import allure
from conftest import driver
from pages.auth_page import AuthPage
from pages.forgot_pas_page import  ForgotPasPage
from faker import Faker
from pages.reset_pas_page import ResetPasPage
from data import Data

faker = Faker()

class TestRestorePassword:
    @allure.title('Проверка кнопки "Восстановить пароль"')
    @allure.description('Нажатие на кнопку и проверка, что осуществился переход на страницу восстановления пароля')
    def test_click_restore_password_button(self, driver):
        auth_page = AuthPage(driver)
        auth_page.navigate_auth_url()
        auth_page.click_restore_password_button()
        auth_page.wait_go_to_forgot_pas_url()
        current_url = auth_page.get_current_url_method()
        assert current_url == Data.FORGOT_PAS_URL


    @allure.title('Проверка кнопки "Восстановить"')
    @allure.description('Ввод имейла, нажатие на кнопку и проверка, что осуществился переход на следующую страницу восстановления пароля')
    def test_click_restore_button(self, driver):
        email = faker.email()
        forgot_pas_page = ForgotPasPage(driver)
        forgot_pas_page.navigate_forgot_pas_url()
        forgot_pas_page.set_email(email)
        forgot_pas_page.click_restore_button()
        forgot_pas_page.wait_go_to_reset_pas_url()
        current_url = forgot_pas_page.get_current_url_method()
        assert current_url == Data.RESET_PAS_URL

    @allure.title('Проверка кнопки "Показать\скрыть пароль"')
    @allure.description('Нажатие на кнопку и проверка, что поле подсветилось')
    def test_click_show_hide_password_button(self, driver):
        forgot_pas_page = ForgotPasPage(driver)
        forgot_pas_page.navigate_forgot_pas_url()
        forgot_pas_page.click_restore_button()
        forgot_pas_page.wait_go_to_reset_pas_url()
        reset_pas_page = ResetPasPage(driver)
        reset_pas_page.click_show_hide_password_button()
        assert reset_pas_page.active_field_password_is_displayed() is True