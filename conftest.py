import pytest
from selenium import webdriver
from constants import Constants
from locators.auth_page_locators import LocatorsAuth
from locators.main_page_locators import Locators
import json
import requests
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from data import Data

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()

    browser.get(Data.URL)
    yield browser
    browser.quit()


@pytest.fixture
def reg():
    payload = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD,
        "name": Constants.NAME
    }
    payload_string = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(Data.REG_URL, data=payload_string, headers=headers)
    r = response.json()
    token = r['accessToken']
    yield token
    headers = {'Authorization': token}
    requests.delete(Data.DEL_URL, headers=headers)

@pytest.fixture
def log(driver, reg):
    auth_page = AuthPage(driver)
    auth_page.navigate_url_method(Data.AUTH_URL)
    auth_page.send_keys_method(LocatorsAuth.EMAIL_FIELD, Constants.EMAIL)
    auth_page.send_keys_method(LocatorsAuth.PASSWORD_FIELD, Constants.PASSWORD)
    auth_page.click_method(LocatorsAuth.LOGIN_BUTTON)

@pytest.fixture
def create_order(driver, log):
    main_page = MainPage(driver)
    main_page.wait_element_to_be_visible_method(Locators.ANY_BUN)
    main_page.drag_and_drop_method(Locators.ANY_BUN, Locators.BURGER_CONSTRUCTOR)
    main_page.click_method(Locators.PLACE_AN_ORDER_BUTTON)
    main_page.wait_element_to_be_clickable_method(Locators.ORDER_POP_UP_WINDOW)
    main_page.click_java_method(Locators.X_BUTTON)

