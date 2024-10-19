from lib2to3.pgen2 import driver

import pytest
import time
import allure
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage


class TestLogin:
    @allure.epic("vwo login Test")
    @allure.feature("Login page;-negative case")
    @pytest.mark.usefixtures("setup")
    def test_login_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        time.sleep(8)
        loginpage.login_to_vwo(user="admin" , pwd= "admin")
        time.sleep(10)
        error_message = loginpage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"

    @allure.epic("vwo login Test")
    @allure.feature("Login page-positive case")
    @pytest.mark.usefixtures("setup")
    def test_login_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        time.sleep(8)
        loginpage.login_to_vwo(user=self.username, pwd=self.password)
        time.sleep(10)
        dashboard = DashboardPage(driver)
        assert "Dashboard" in driver.title
        assert "NITESH KUMAR" in dashboard.user_logged_in_text()
