# Page Class
from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    # page locators

    user_logged_in = (By.XPATH, "//span[@data-qa='lufexuloga']")


    #Page actiones methods

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def user_logged_in_text(self):
        return self.get_user_logged_in().text

    def get_error_message_text(self):
        return self.get_error_message().text