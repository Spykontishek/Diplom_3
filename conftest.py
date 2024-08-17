import pytest
from selenium import webdriver
from constants import Constants
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.auth_page_locators import LocatorsAuth
from locators.main_page_locators import Locators
import json
import requests
from selenium.webdriver import ActionChains


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()

    browser.get(Constants.URL)
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
    response = requests.post(Constants.REG_URL, data=payload_string, headers=headers)
    r = response.json()
    token = r['accessToken']
    yield token
    headers = {'Authorization': token}
    requests.delete(Constants.DEL_URL, headers=headers)

@pytest.fixture
def log(driver, reg):
    driver.get(Constants.AUTH_URL)
    driver.find_element(*LocatorsAuth.EMAIL_FIELD).send_keys(Constants.EMAIL)
    driver.find_element(*LocatorsAuth.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
    driver.find_element(*LocatorsAuth.LOGIN_BUTTON).click()

@pytest.fixture
def create_order(driver, log):
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ANY_BUN))
    action = ActionChains(driver)
    action.drag_and_drop(driver.find_element(*Locators.ANY_BUN), driver.find_element(*Locators.BURGER_CONSTRUCTOR)).perform()
    driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.ORDER_POP_UP_WINDOW))
    element = driver.find_element(*Locators.X_BUTTON)
    driver.execute_script("arguments[0].click();", element)
