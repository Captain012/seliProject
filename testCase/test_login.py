# test_login
import allure
import pytest

from utils.handle_getYaml import get_yaml_data
from utils.handle_path import GetPath
from pages.loginPage import Login
from config.env import Env
import os

@allure.epic('宝利商店')
@allure.feature('登录模块')
class TestLogin:
    @pytest.mark.parametrize(('title,username,password,locator,exp_res'),get_yaml_data(GetPath.data_path/'data_login.yaml'))
    @allure.title('{title}')
    @pytest.mark.logincase
    @pytest.mark.flaky(rerun = 3,rerun_delay = 2)
    def test_login(self,title,username,password,locator,exp_res):
        with allure.step('1、实例化登录'):
            login_page = Login()
        with allure.step('2、获取登录页面'):
            login_page.get_login_page()
        with allure.step('3、输入账号密码'):
            mainpage = login_page.login(username,password)
        with allure.step('4、断言'):
            assert login_page.get_element_text(locator) == exp_res
        with allure.step('5、断言后的处理'):
            with pytest.assume:
                if mainpage.driver.current_url == Env.MAINPAGE:
                    mainpage.quit_to_login()






if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir',GetPath.report_path,'--clean-alluredir'])
    # os.system(f'allure generate {GetPath.allu_rep_path} -o {GetPath.allu_rep_path} --clean')
    # os.system(f'allure serve {GetPath.report_path}')

