import os,sys

import pytest
import time

sys.path.append(os.getcwd())
from page.page import Page
from base.get_driver import get_driver
from base.get_data import Get_Data
from selenium.common.exceptions import TimeoutException
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

class Test_login:
    def setup_class(self):
        # self.page_obj = Page(get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity"))
        self.page_obj1 = Page(get_driver())

    def teardown_class(self):
        self.page_obj1.driver.quit()

    # @pytest.mark.parametrize("test_num,phone,passwd,tag,tag_message,expect_result", get_login_data())
    # def test_001_001(self,test_num,phone,passwd,tag,tag_message,expect_result):
    #     self.page_obj1.get_home_obj().click_my_btn()
    #     self.page_obj1.get_sign_obj().click_exists_btn()
    #     self.page_obj1.get_login_obj().login_user(phone, passwd)
    #     if tag:
    #         try:
    #             assert expect_result in self.page_obj1.get_person_obj().person_coupons()
    #             self.page_obj1.get_person_obj().get_setting()
    #             self.page_obj1.get_setting_obj().login_out(tag)
    #
    #         except:
    #             assert False
    #     else:
    #         try:
    #             assert expect_result in self.page_obj1.get_setting_obj().get_toast(tag_message)
    #         except:
    #             assert False
    #         finally:
    #             self.page_obj1.get_login_obj().out_btn_user()

# if __name__ == '__main__':
#     pytest.main("-s test_01.py")







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
        # 点击我
        self.page_obj1.get_home_obj().click_my_btn()
        self.page_obj1.get_sign_obj().click_exists_btn()
        self.page_obj1.get_login_obj().login_user(phone, passwd)
        # 判断成功失败用例
        if tag:
            # 预期成功用例
            try:
                # 优惠券
                coupons = self.page_obj1.get_person_obj().person_coupons()
                try:
                    # 断言
                    assert coupons == expect_result
                except AssertionError as e:
                    print(e.__str__())
                # 执行退出操作
                # 点击设置
                self.page_obj1.get_person_obj().get_setting()
                time.sleep(3)
                self.page_obj1.get_setting_obj().login_out(1)

            except TimeoutException as e:
                # 关闭登录页面
                self.page_obj1.get_login_obj().out_btn_user()
                assert False

        else:
            # 预期失败的用例
            try:
                # 获取toast消息
                toast_message = self.page_obj1.get_setting_obj().get_toast(tag_message)
                # 获取登录按钮是否存在
                if_login = self.page_obj1.get_login_obj().if_login_btn_exits()
                # 断言
                assert if_login and toast_message == expect_result

            except TimeoutException as e:
                assert False

            finally:
                # 关闭登录页面
                self.page_obj1.get_login_obj().out_btn_user()