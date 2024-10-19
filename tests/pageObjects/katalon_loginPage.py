from selenium import webdriver
from selenium.webdriver.common.by import By


class Katalon_login():
    def __init__(self, driver):
        self.driver = webdriver.Chrome()

    # Page locators
    make_appointment = (By.ID, "btn-make-appointment")
    username_katalon = (By.ID, "txt-username")
    password_katalon = (By.ID, "txt-password")
    login_button = (By.ID, "btn-login")

    # page actions
    def get_make_appointment(self):
        return self.driver.find_element(*Katalon_login.make_appointment)

    # def get_username(self):
    #     return self.driver.find_element(*Katalon_login.username_katalon)
    #
    # def get_password(self):
    #     return self.driver.find_element(*Katalon_login.password_katalon)
    #
    # def click_login(self):
    #     return self.driver.find_element(*Katalon_login.login_button)

    # page main actions
    def click_homepage(self):
        self.get_make_appointment().click()


    #def login_to_katalon(self, username, password):
        # self.get_username().send_keys("username")
        # self.get_password().send_keys("password")
        # self.click_login().click()

    # def make_appointment_first(self):
       # self.click_make_appointment().click()



