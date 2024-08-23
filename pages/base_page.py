from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_method(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_method(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

    def drag_and_drop_method(self, start_locator_element, finish_locator_element):
        action = ActionChains(self.driver)
        drag = self.driver.find_element(*start_locator_element)
        drop = self.driver.find_element(*finish_locator_element)
        action.drag_and_drop(drag, drop).perform()


    def navigate_url_method(self, constants_url):
        self.driver.get(constants_url)

    def wait_url_to_be_visible_method(self, constants_url):
        WebDriverWait(self.driver, 3).until(EC.url_to_be(constants_url))

    def wait_element_to_be_visible_method(self, locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def wait_element_to_be_clickable_method(self, locator):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    def click_java_method(self,locator): # Очень баганный сайт, многие обычные питонские команды для клика валили тесты, пришлось создать несколько джава методов
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def element_is_displayed_method(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def wait_all_elements_to_be_visible_method(self, locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(locator))

    def get_all_elements_texts_method(self,locator):
        elements = self.driver.find_elements(*locator)
        return [element.text for element in elements]

    def get_element_text_method(self,locator):
        return self.driver.find_element(*locator).text

    def wait_element_to_be_invisible(self,locator):
            WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(locator))

