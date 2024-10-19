import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    # Page Locators

    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    login_button = (By.ID, "js-login-btn")
    forgot_password = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    error_message = (By.XPATH, "//div[@id='js-notification-box-msg']")
    remember_me = (By.XPATH, "//label[@for ='checkbox-remember']")

    # Page Actions-methods

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_forgot_password_link(self):
        return self.driver.find_element(*LoginPage.forgot_password)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def get_remember_me_checkbox(self):
        return self.driver.find_element(*LoginPage.remember_me)

    # Page Action - main ACTION

    def login_to_vwo(self, user, pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_login_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text
