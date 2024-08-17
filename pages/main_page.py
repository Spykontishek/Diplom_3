from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators.main_page_locators import Locators
from selenium.webdriver import ActionChains


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_personal_account_button(self):
        self.driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    def click_personal_account_button_java(self):
        element = self.driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_go_to_personal_account_url(self):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Constants.PERSONAL_ACC_URL))

    def click_constructor_button(self):
        self.driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    def click_order_feed_button(self):
        self.driver.find_element(*Locators.ORDER_FEED_BUTTON).click()

    def click_order_feed_button_java(self):
        element = self.driver.find_element(*Locators.ORDER_FEED_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_order_feed_button_to_be_clickable(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(Locators.ORDER_FEED_BUTTON))

    def wait_go_to_order_feed_url(self):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(Constants.ORDER_FEED_URL))

    def click_on_ingredient(self):
        self.driver.find_element(*Locators.ANY_INGREDIENT).click()

    def wait_ingredient_pop_up_window_is_displayed(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.INGREDIENT_POP_UP_WINDOW))

    def click_x_button(self):
        self.driver.find_element(*Locators.X_BUTTON).click()

    def click_on_x_button_java(self):
        element = self.driver.find_element(*Locators.X_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_pop_up_window_is_not_displayed(self):
        return WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(Locators.INGREDIENT_POP_UP_WINDOW))

    def move_ingredient_to_burger_constructor(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*Locators.ANY_INGREDIENT), self.driver.find_element(*Locators.BURGER_CONSTRUCTOR)).perform()

    def wait_for_any_bun_to_be_visible(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.ANY_BUN))

    def move_bun_to_burger_constructor(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*Locators.ANY_BUN), self.driver.find_element(*Locators.BURGER_CONSTRUCTOR)).perform()

    def click_on_place_an_order_button(self):
        self.driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON).click()

    def wait_order_pop_up_window_is_displayed(self):
         WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_POP_UP_WINDOW))

    def personal_account_button_is_clickable(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON))


