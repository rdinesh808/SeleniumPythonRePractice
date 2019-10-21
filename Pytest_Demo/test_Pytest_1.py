from selenium import webdriver
import time
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.find_element_by_xpath("//md-icon[@md-svg-icon='logout']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//td/div[text()='Yes']").click()

    def test_login(self,test_setup):
        driver.get("https://qa.gsihealth.net")
        driver.find_element_by_name("UserID").send_keys("prabhaharan.velu@gsihealth.com")
        time.sleep(1)
        driver.find_element_by_name("Password").send_keys("Imax123#")
        time.sleep(1)
        driver.find_element_by_xpath("//button/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[text()='Got it']").click()
        time.sleep(1)

    def test_teardown(self):
        driver.close()
        driver.quit()
        print("Test Completed..!!")