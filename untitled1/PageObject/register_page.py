from parameterized import parameterized
from selenium.webdriver.common.by import By
from Common.data_processing import data_processing
from Common.readini import Config
from Utils.logger import log
from base.base_page import BasePage
from selenium import webdriver
import time

class Reg_Page(BasePage):
    # 初始化方法
    def __init__(self):
        super().__init__()
        self.filepath = r'C:\Users\Administrator\PycharmProjects\untitled1\data\location.ini'
        self.url = Config(self.filepath).get_data('website','home_url')
        self.entrance = Config(self.filepath).get_data('reg_location','reg_entrance')     # 定位注册入口  # 把括号去掉也可以,*代表收集参数
        self.Reg_username = Config(self.filepath).get_data('reg_location','reg_username')    # 定位用户名输入框
        self.Reg_password = Config(self.filepath).get_data('reg_location','reg_password')     # 定位密码输入框
        self.Reg_passwordConfirm = Config(self.filepath).get_data('reg_location','reg_passwordConfirm')     # 定位确认密码输入框
        self.Reg_button = Config(self.filepath).get_data('reg_location','reg_button')     # 定位确认注册按钮
        self.actual_location = Config(self.filepath).get_data('reg_location','actual_location')    # 检查点定位
    # url = "http://localhost:1080/webtours/"
    # entrance = (By.LINK_TEXT, "sign up now")  # 定位注册入口  # 把括号去掉也可以,*代表收集参数
    # Reg_username = (By.NAME, "username")  # 定位用户名输入框
    # Reg_password = (By.NAME, "password")  # 定位密码输入框
    # Reg_passwordConfirm = (By.NAME, "passwordConfirm")  # 定位确认密码输入框
    # search_button = (By.NAME, "register")  # 定位确认注册按钮
    # actual_location = (By.XPATH, '/html/body/blockquote')  # 检查点定位
    def reg_page(self,yhm,mm):
        # 进入网页
        self.visit(self.url)
        # 切换框架
        self.frame(Config(self.filepath).get_data('reg_location','reg_frame_1'))
        self.frame(Config(self.filepath).get_data('reg_location','reg_frame_2'))
        # 进入注册页面
        self.click(self.entrance)
        # 输入注册用户名
        self.send_keys(self.Reg_username, yhm)
        # 输入注册密码
        self.send_keys(self.Reg_password, mm)
        # 确定注册密码
        self.send_keys(self.Reg_passwordConfirm, mm)
        # 定位注册按钮
        self.click(self.Reg_button)
        # 检查点
        expect_01 = 'Thank you,' + " " + yhm
        actual = self.text(self.actual_location)
        # self.check(expect,actual)
        # assert actual in expect_01
        try :
            assert expect_01 in actual
            log.info('注册成功')
            print('注册成功')
        # except AssertionError as e:
        except Exception as e:
            log.info('注册失败:%s'%'AssertionError')
            print('注册失败')
            raise (e)
            # raise ('注册失败:%s'%'AssertionError')
        finally:
            print('执行结束')

if __name__=="__main__":
    Reg_Page().reg_page(yhm = "zhsan1",mm = 1)