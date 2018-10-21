import time

from base.base import Base
import page

class Setting_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)


    def login_out(self, tag):
        self.swipe_page(1)
        self.base_element_click(page.logout_btn_id)
        if tag == 1:
            self.base_element_click(page.logout_acc_btn_id)
        else:
            self.base_element_click(page.log_out_miss_btn_id)