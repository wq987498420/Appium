from base.base import Base
import page

class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login_user(self, user, password):
        self.base_element_send(page.login_account_id, user)
        self.base_element_send(page.login_passwd_id, password)
        self.base_element_click(page.login_btn_id)

    def out_btn_user(self):
        self.base_element_click(page.out_btn_id)

    def if_login_btn_exits(self):
        self.base_element(page.login_btn_id)