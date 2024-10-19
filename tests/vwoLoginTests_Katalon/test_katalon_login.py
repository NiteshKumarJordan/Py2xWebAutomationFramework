import time

import allure
import pytest
from tests.pageObjects.katalon_loginPage import Katalon_login


class Test_Case_Katalon:

    @pytest.mark.usefixtures("setup")
    def katalon_login_positive(self, setup):
        driver = setup
        driver.get("https://katalon-demo-cura.herokuapp.com")
        khp = Katalon_login(driver)
        khp.click_homepage()
        time.sleep(5)
        assert "profile.php#login" in driver.current_url
        time.sleep(3)
