import sys, os
sys.path.append(os.getcwd())
import pytest
from base.get_driver import get_driver
from base.get_data import Get_Data
from page.page import Page

"""
[(用例编号,手机号,密码,tag,tag_message,预期结果)]
"""
def get_login_data():
    # 结果列表
    login_list = []
    data = Get_Data().get_yaml_data("aolai.yml")
    # return data
    for i in data.keys():
        login_list.append((i, data.get(i).get("phone"), data.get(i).get("passwd"),
                           data.get(i).get("tag"), data.get(i).get("tag_message"),
                           data.get(i).get("expect_result")))
    return login_list

class Test_Login:
    def setup_class(self):
        self.page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))
    
    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.mark.parametrize("test_num,phone,passwd,tag,tag_message,expect_result", get_login_data())
    def test_login(self, test_num, phone, passwd, tag, tag_message, expect_result):
        """

        :param test_num: 用例编号
        :param phone: 输入手机号
        :param passwd: 输入密码
        :param tag: 标记成功用例 1 成功用例  None 失败用例
        :param tag_message: 获取toast消息方法参数
        :param expect_result:预期结果
        :return:
        """
        pass

