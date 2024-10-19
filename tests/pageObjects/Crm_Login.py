from selenium.webdriver.common.by import By


class Login_Page_Crm():
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.ID, "LoginForm_username")
    password = (By.ID, "LoginForm_password")
    sign_in = (By.ID, "lgBtn")

    # Page Actions-methods

    def get_username(self):
        return self.driver.find_element(*Login_Page_Crm.username)

    def get_password(self):
        return self.driver.find_element(*Login_Page_Crm.password)

    def get_sign_in_button(self):
        return self.driver.find_element(*Login_Page_Crm.sign_in)

    # Page Actions-main ACTION

    def login_to_crm(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_sign_in_button().click()
