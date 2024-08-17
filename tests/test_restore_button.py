import allure
from conftest import driver
from pages.forgot_pas_page import  ForgotPasPage
from constants import Constants
from faker import Faker

faker = Faker()


class TestRestoreButton:
    @allure.title('Проверка кнопки "Восстановить"')
    @allure.description('Ввод имейла, нажатие на кнопку и проверка, что осуществился переход на следующую страницу восстановления пароля')
    def test_click_restore_button(self, driver):
        email = faker.email()
        driver.get(Constants.FORGOT_PAS_URL)
        forgot_pas_page = ForgotPasPage(driver)
        forgot_pas_page.set_email(email)
        forgot_pas_page.click_restore_button()
        forgot_pas_page.wait_go_to_reset_pas_url()
        current_url = driver.current_url
        assert current_url == Constants.RESET_PAS_URL