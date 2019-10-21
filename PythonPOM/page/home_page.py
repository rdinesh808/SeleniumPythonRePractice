from PythonPOM.Locators.locator import ele_locate
class HomePages():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_button_id = ele_locate.welcome_button_id
        self.logout_button_text = ele_locate.logout_button_text


    def welcome_page(self):
        self.driver.find_element_by_id(ele_locate.welcome_button_id).click()

    def logout_page(self):
        self.driver.find_element_by_link_text(ele_locate.logout_button_text).click()
