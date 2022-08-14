from configparser import ConfigParser
from selenium.webdriver.common.by import By
class Config():
    def __init__ (self,filepath):
        self.filepath=filepath
        self.config=ConfigParser()
        self.config.read(filepath, encoding = 'UTF-8')
    def get_data(self,sections,key) :
        return (eval(self.config.get(sections,key)))
if __name__ == "__main__":
       print(Config(filepath = r'C:\Users\Administrator\PycharmProjects\untitled1\data\location.ini').get_data('website','home_url'))
       # print(type(Config().get_data('website','home_url')))
       # print(Config().get_data('reg_location','reg_entrance'))
       # print(type(Config().get_data('reg_location','reg_entrance')))
       # print(Config().get_data('reg_location', 'reg_username'))
       # print(Config().get_data('reg_location', 'reg_password'))
       # print(Config().get_data('reg_location', 'reg_passwordConfirm'))
       # print(Config().get_data('reg_location', 'reg_button'))
       # print(Config().get_data('reg_location', 'actual_location'))
       a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
       print(type(a))
       b = eval(a)
       print(type(b))
       print(b)

