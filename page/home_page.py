from base.base import Base
import page

class Home_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_my_btn(self):
        self.base_element_click(page.my_btn_id)
