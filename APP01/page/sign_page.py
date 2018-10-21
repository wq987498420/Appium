from base.base import Base
import page

class Sign_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exists_btn(self):
        self.base_element_click(page.exits_account_id)