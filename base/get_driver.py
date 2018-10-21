from appium import webdriver

def get_driver():
    dict_1 = {}
    dict_1['platformName'] = 'android'
    dict_1['platformVersion'] = '5.1'
    dict_1['deviceName'] = 'sanxing'
    dict_1['appPackage'] = "com.yunmall.lc"
    dict_1['appActivity'] = "com.yunmall.ymctoc.ui.activity.MainActivity"
    dict_1['automationName'] = 'Uiautomator2'
    return webdriver.Remote('http://192.168.45.35:4723/wd/hub', dict_1)
