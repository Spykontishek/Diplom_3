from locators.main_page_locators import Locators
import allure
from pages.base_page import BasePage
from data import Data
class MainPage(BasePage):


    @allure.step('клик по кнопке "Личный Кабинет"')
    def click_personal_account_button(self):
        self.click_method(Locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('клик по кнопке "Личный Кабинет" с помощью Java')
    def click_personal_account_button_java(self):
        self.click_java_method(Locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Ожидания перехода на страницу личного кабинета')
    def wait_go_to_personal_account_url(self):
        self.wait_url_to_be_visible_method(Data.PERSONAL_ACC_URL)

    @allure.step('клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_method(Locators.CONSTRUCTOR_BUTTON)

    @allure.step('клик по кнопке "Лента Заказов"')
    def click_order_feed_button(self):
        self.click_method(Locators.ORDER_FEED_BUTTON)

    @allure.step('клик по кнопке "Лента Заказов" с помощью Java')
    def click_order_feed_button_java(self):
        self.click_java_method(Locators.ORDER_FEED_BUTTON)
    @allure.step('ожидание пока кнопка "Лента Заказов" станет кликабельна')
    def wait_order_feed_button_to_be_clickable(self):
        self.wait_element_to_be_clickable_method(Locators.ORDER_FEED_BUTTON)

    @allure.step('Ожидания перехода на страницу ленты заказов')
    def wait_go_to_order_feed_url(self):
        self.wait_url_to_be_visible_method(Data.ORDER_FEED_URL)

    @allure.step('клик на ингридиент')
    def click_on_ingredient(self):
        self.click_method(Locators.ANY_INGREDIENT)

    @allure.step('ожидание пока всплывающее окно с информацией об ингридиенте станет видимым')
    def wait_ingredient_pop_up_window_is_displayed(self):
        self.wait_element_to_be_visible_method(Locators.INGREDIENT_POP_UP_WINDOW)

    @allure.step('клик по кнопке крестик всплывающего окна')
    def click_x_button(self):
        self.click_method(Locators.X_BUTTON)

    @allure.step('клик по кнопке крестик всплывающего окна с помощью Java')
    def click_on_x_button_java(self):
        self.click_java_method(Locators.X_BUTTON)

    @allure.step('ожидание пока всплывающее окно с информацией об ингридиенте закроется')
    def wait_pop_up_window_is_not_displayed(self):
        self.wait_element_to_be_invisible(Locators.INGREDIENT_POP_UP_WINDOW)

    @allure.step('перетаскивание ингридиента в конструктор для оформления заказа')
    def move_ingredient_to_burger_constructor(self):
        self.drag_and_drop_method(Locators.ANY_INGREDIENT,Locators.BURGER_CONSTRUCTOR)

    @allure.step('ожидание пока булка из конструктора станет видимой')
    def wait_for_any_bun_to_be_visible(self):
        self.wait_element_to_be_visible_method(Locators.ANY_BUN)

    @allure.step('перетаскивание булки в конструктор для оформления заказа')
    def move_bun_to_burger_constructor(self):
        self.drag_and_drop_method(Locators.ANY_BUN,Locators.BURGER_CONSTRUCTOR)

    @allure.step('клик по кнопке Оформить заказ')
    def click_on_place_an_order_button(self):
        self.click_method(Locators.PLACE_AN_ORDER_BUTTON)

    @allure.step('ожидание пока всплывающее окно с информацией о заказе станет видимым')
    def wait_order_pop_up_window_is_visible(self):
         self.wait_element_to_be_visible_method(Locators.ORDER_POP_UP_WINDOW)

    @allure.step('проверка, что всплывающее окно открылось')
    def pop_up_is_displayed(self):
        self.element_is_displayed_method(Locators.ORDER_POP_UP_WINDOW)

    @allure.step('ожидание пока кнопка "Личный Кабинет станет кликабельной')
    def personal_account_button_is_clickable(self):
        self.wait_element_to_be_clickable_method(Locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('ожидание пока увеличенный счетчик ингридиента станет видимым')
    def counter_of_ingredient_is_visible(self):
        self.wait_all_elements_to_be_visible_method(Locators.COUNTER_OF_INGREDIENT)

    @allure.step('проверка, что счетчик ингридиента увеличился с 0-ля до 1-ого')
    def counter_of_ingredient_is_displayed(self):
        return self.element_is_displayed_method(Locators.COUNTER_OF_INGREDIENT)

    @allure.step('Переход на главную страницу')
    def navigate_main_url(self):
        self.navigate_url_method(Data.URL)






