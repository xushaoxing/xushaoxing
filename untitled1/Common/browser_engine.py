from selenium import webdriver
from Common.config_manage import ConfigManager


class BrowserEngine(object):

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ConfigManager().CHROME_DRIVER)
    # Chrome浏览器驱动
    # self.driver = webdriver.Edge(executable_path=config_manager.EDGE_DRIVER)
    # Edge浏览器驱动


browser_engine = BrowserEngine().driver
print(browser_engine)
