# from appium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver

    def base_element(self, loc, timeout=15, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def base_elements(self, loc, timeout=15, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def base_element_click(self,loc, timeout=15, poll_frequency=1.0):
        self.base_element(loc, timeout, poll_frequency).click()

    def base_element_send(self,loc,text,timeout=15, poll_frequency=1.0):
        ment_send = self.base_element(loc,timeout, poll_frequency)
        ment_send.clear()
        ment_send.send_keys(text)

    def swipe_page(self,tag):
        screen = self.driver.get_window_size()
        width = screen.get("width")
        height = screen.get("height")
        if tag == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

    def get_toast(self,mess):
        toast_xapth = "//*[contains(@text,'{}')]".format(mess)
        return self.base_element((By.XPATH,toast_xapth),timeout=5,poll_frequency=0.5).text