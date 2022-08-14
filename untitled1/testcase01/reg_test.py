import unittest
import parameterized
from selenium import webdriver
from Common.data_processing import data_processing
from PageObject.register_page import Reg_Page
from base.base_page import BasePage
from Utils.logger import log

class Reg(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        BasePage().maximize()
        # cls.driver = webdriver.Chrome()
        # cls.se = Reg_Page(cls.driver)
    @classmethod
    def tearDownClass(cls) -> None:
        BasePage().close()
    data=data_processing().open_read()
    # 用户已注册验证

    @parameterized.parameterized.expand(data)
    def test_reg_01(self,yhm,mm):
        Reg_Page().reg_page(yhm,mm)
        # log.info("注册")
        # self.se.reg_page(yhm,mm)
# if __name__ =="__main__":
#     unittest.main(verbosity=2)

# def reg_test( yhm, mm):
#     Reg_Page().reg_page(yhm, mm)
# reg_test(yhm='zhsanq', mm=1)