import os,sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from page.page import Page
from base.get_driver import get_driver

# 配合使用
page_obj = Page(get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity"))
page_obj.get_home_obj().click_my_btn()
page_obj.get_sign_obj().click_exists_btn()
page_obj.get_login_obj().login_user("17606863713", "wq521521")
assert "我的优惠券" in page_obj.get_person_obj().person_coupons()


# def get_toast(mess):
#     mess_xapth = "//*[contains(@text,'{}')]".format(mess)
#     return page_obj.get_home_obj().base_element((By.XPATH,mess_xapth),timeout=5,poll_frequency=0.5).text
# print(get_toast('此用户'))

page_obj.driver.quit()