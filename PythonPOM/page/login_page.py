from PythonPOM.Locators.locator import ele_locate

class Loginpages():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = ele_locate.username_textbox_id
        self.password_textbox_id = ele_locate.password_textbox_id
        self.login_button_id = ele_locate.login_button_id

    def enter_username(self,username):
        self.driver.find_element_by_id(ele_locate.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(ele_locate.password_textbox_id).send_keys(password)

    def login_button(self):
        self.driver.find_element_by_id(ele_locate.login_button_id).click()