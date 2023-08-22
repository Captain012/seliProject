# projectList
from pages.pmPages.projectListPage import ProjectListPage
from pages.pmPages.projectAddPage import ProjectAddPage
from pages.mainPage import MainPage
import pytest
import allure
from utils.handle_getRandom import get_random_str
from random import choice
from utils.handle_path import GetPath
import os

@allure.epic('宝利商店')
@allure.feature('商品管理')
class TestProjectAdd():
    @allure.story('添加商品')
    @pytest.mark.addcase
    def test_projectadd(self,auto_login:MainPage):
        with allure.step('1、登录宝利'):
            main_page = auto_login
        with allure.step('2、跳转到商品页面'):
            add_page = main_page.goto_page('添加商品')
        with allure.step('3、添加商品'):
            name = '商品名' + get_random_str(5)
            title = '副标题' + get_random_str(5)
            add_page.add_project(1,1,name,title,1)
        with allure.step('4、返回到首页'):
            add_page.return_to_home()
        with allure.step('5、跳转到商品列表'):
            list_page = main_page.goto_page('商品列表')
        with allure.step('6、断言'):
            assert list_page.get_first_project_name() == name
    @allure.story('品牌管理')
    @pytest.mark.brandcase
    def test_brandmanage(self,auto_login:MainPage):
        with allure.step('1、登录宝利'):
            main_page = auto_login
        with allure.step('2、跳转到品牌管理'):
            brand_manage_page = main_page.goto_page('品牌管理')
        with allure.step('3、随机获取品牌名'):
            current_list = brand_manage_page.get_name_list()
            tag = choice(current_list)
            # print(current_list)
        with allure.step('4、查询品牌'):
            brand_manage_page.query_list(tag)
        with allure.step('5、获取查询结果的品牌列表'):
            list_text = brand_manage_page.get_name_list()
            # print(list_text)
        with allure.step('6、断言'):
            for i in list_text:
                if tag in i:
                    assert True
                else:
                    assert False





if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir',GetPath.report_path,'--clean-alluredir'])
    # os.system(f'allure serve {GetPath.report_path}')








