from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://www.google.com")

element = driver.find_element_by_name("q")

element.send_keys("Selenium Automation")

ActionChains(driver).send_keys(Keys.RETURN).perform()

print(driver.title)

time.sleep(3)

driver.close()

driver.quit()

print("Test Completed..!!!")