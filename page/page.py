from page.home_page import Home_Page
from page.setting_page import Setting_Page
from page.login_page import Login_Page
from page.person_page import Person_Page
from page.sign_page import Sign_Page

class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_home_obj(self):
        return Home_Page(self.driver)
    
    def get_setting_obj(self):
        return Setting_Page(self.driver)

    def get_login_obj(self):
        return Login_Page(self.driver)

    def get_person_obj(self):
        return Person_Page(self.driver)

    def get_sign_obj(self):
        return Sign_Page(self.driver)