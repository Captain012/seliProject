# login
import time

from common.basePage import BasePage
from time import sleep
from config.env import Env
from pages.mainPage import MainPage
class Login(BasePage):
    pass
    def get_login_page(self):
        self.open_url(Env.HOST)
        return self
    def login(self,username,passwrod):
        # print(self.elements)
        self.input(self.user_name,username)
        self.input(self.pass_word, passwrod)
        self.click(self.button_login)
        return MainPage()




if __name__ == '__main__':
    login_page = Login()
    login_page.get_login_page()
    login_page.login('朝天宫149','123456')

    # print(login_page.user_name)

