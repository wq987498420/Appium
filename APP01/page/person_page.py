from base.base import Base
import page

class Person_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def person_coupons(self):
        return self.base_element(page.person_coupons_id).text

    def get_setting(self):
        self.base_element_click(page.setting_btn_id)