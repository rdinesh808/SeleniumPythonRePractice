import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        path = "C:\\Users\\computer003\\Desktop\\Selenium Python Re-Practice\\Driver\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=path)
        driver.implicitly_wait(10)
        driver.maximize_window()

    def test_one(self):
        driver.get("https://www.google.com")
        element = driver.find_element_by_name("q")
        element.send_keys("Selenium Automation Python")
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        print(driver.title)
        time.sleep(3)

    def test_two(self):
        driver.get("https://www.google.com")
        element = driver.find_element_by_name("q")
        element.send_keys("Selenium Automation Java")
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        print(driver.title)
        time.sleep(3)

    def test_three(self):
        driver.get("https://www.google.com")
        element = driver.find_element_by_name("q")
        element.send_keys("Selenium Automation JavaScript")
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        print(driver.title)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()
        print("Test Completed..!!!")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/computer003/Desktop/Selenium Python Re-Practice/PythonUnittest/HTML Report"))