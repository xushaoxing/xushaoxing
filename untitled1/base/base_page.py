'''
基类：提供各个常用的已封装好的函数，便于后续的页面对象类进行调用。
selenium中常用的函数:元素定位、输入、点击、访问URL、等待、关闭
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.Screenshot_page import Screenshot

class BasePage():
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    driver = webdriver.Chrome()
    # 最大化
    def maximize(self):
        self.driver.maximize_window()
    # 访问URL
    def visit(self, url):
        self.driver.get(url)
    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)  # *代表收集参数
    # 输入
    def send_keys(self, loc, value):
        self.locator(loc).send_keys(value)
    # 点击
    def click(self, loc):
        self.locator(loc).click()
    # 文本
    def text(self,loc):
        return self.locator(loc).text
    # 切换框架
    def frame(self,name):
        self.driver.switch_to.frame(name)
    # 切换为主框架
    def switch_to_default_content(self,name):
        self.driver.switch_to.default_content(name)
    # 等待
    def wait(self, time):
        sleep(time)
    # 关闭
    def close(self):
        self.driver.quit()
    # 检查点
    def check(self,expect,actual):
        if expect in actual:
            result="测试通过"
            print(result)
        else:
            result="测试失败"
            Screenshot().fail_screenshot(result)
            print(result)
if __name__=="__main__":
    search_input = (By.NAME, 'wd')
    BasePage().visit('http://www.baidu.com')
    BasePage().click(search_input)
    BasePage().send_keys(search_input,32132)
