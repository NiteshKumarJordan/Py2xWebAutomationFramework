from lib2to3.pgen2 import driver

import pytest
import time

import allure

from tests.pageObjects import dashboardPage
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("vwo login Test")
@allure.feature("Login page")
@allure.story("Negative login test")
@allure.description("Test to validate negative login")
@pytest.mark.negative
def test_login_negative(setup):
    driver = setup
    loginpage = LoginPage(driver)
    time.sleep(8)
    loginpage.login_to_vwo(email="vwo@app.vwo.com", pwd="admin")
    time.sleep(10)
    error_message = loginpage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"

def test_login_positive(setup):
    driver = setup
    loginpage = LoginPage(driver)
    time.sleep(8)
    loginpage.login_to_vwo(email="nitesh.kumar@360realtors.com", pwd="Jordan365@1995")
    time.sleep(10)
    dashboard = DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "NITESH KUMAR" in dashboard.user_logged_in_text()
