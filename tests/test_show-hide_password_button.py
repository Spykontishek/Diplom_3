import allure
from conftest import driver
from pages.reset_pas_page import ResetPasPage
from pages.forgot_pas_page import  ForgotPasPage
from constants import Constants

class TestShowHidePasswordButton:
    ACTIVE_FIELD_PASSWORD = ResetPasPage.ACTIVE_FIELD_PASSWORD
    @allure.title('Проверка кнопки "Показать\скрыть пароль"')
    @allure.description('Нажатие на кнопку и проверка, что поле подсветилось')
    def test_click_show_hide_password_button(self, driver):
        driver.get(Constants.FORGOT_PAS_URL)
        forgot_pas_page = ForgotPasPage(driver)
        forgot_pas_page.click_restore_button()
        forgot_pas_page.wait_go_to_reset_pas_url()
        reset_pas_page = ResetPasPage(driver)
        reset_pas_page.click_show_hide_password_button()
        assert driver.find_element(*self.ACTIVE_FIELD_PASSWORD).is_displayed()