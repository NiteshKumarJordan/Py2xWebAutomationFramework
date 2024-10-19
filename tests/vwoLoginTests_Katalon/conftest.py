from selenium import webdriver
import pytest
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    username = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    katalon_url = os.getenv("KATALON_URL")
    crm_url = os.getenv("360crm_url")
    crm_username = os.getenv("CRM_USERNAME")
    crm_password = os.getenv("CRM_PASSWORD")


    # username_katalon = os.getenv("USERNAME_KATALON")
    # password_katalon = os.getenv("PASSWORD_KATALON")

    # request we are using so that it will be available for other classes.
    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password
    request.cls.base_url = base_url
    request.cls.katalon_url = katalon_url
    request.cls.crm_url = crm_url
    request.cls.crm_username = crm_username
    request.cls.crm_password = crm_password


    # request.cls.username_katalon = username_katalon
    # request.cls.password_katalon = password_katalon

    yield driver
    driver.quit()
