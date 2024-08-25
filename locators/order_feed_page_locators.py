from selenium.webdriver.common.by import By


class Locators:
    ANY_ORDER = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem')]")
    ORDER_FEED_POP_UP_OF_ORDER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    ORDERS_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_list')]//li")
    TOTAL_COMPLETED_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    COMPLETED_ORDERS_FOR_TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]//li")

