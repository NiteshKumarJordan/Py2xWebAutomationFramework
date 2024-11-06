from tests.pageObjects.Crm_Login import Login_Page_Crm
import pytest
import allure_pytest
import allure


class crm_login:
    @pytest.mark.usefixtures("setup")
    @allure.epic("vwo login Test")
    @allure.feature("Login page;-negative case")
    def test_crm_login(self, setup):
        driver = setup
        driver.get(self.crm_url)
        crm_l = Login_Page_Crm(driver)
        crm_l.login_to_crm(username="self.username", password="self.password")
        assert "CRM" in driver.title
        assert "Welcome to CRM" in driver.page_source
