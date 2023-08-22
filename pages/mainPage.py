# main
from common.basePage import BasePage
from pages.pmPages.projectAddPage import ProjectAddPage
from pages.pmPages.projectListPage import ProjectListPage
from pages.pmPages.brandManagePage import BrandManagePage
from time import sleep
class MainPage(BasePage):
    def quit_to_login(self):
        self.click(self.head_selector)
        self.click(self.quit_to_login_button)


    def goto_page(self,page_name):
        # sleep(3)
        self.click(self.project_manage)
        # sleep(3)
        if page_name == '商品列表':
            self.click(self.project_list)
            # sleep(3)
            # self.click(self.project_manage)
            return ProjectListPage()
        if page_name == '添加商品':
            self.click(self.project_add)
            # self.click(self.project_manage)
            return ProjectAddPage()
        if page_name == '品牌管理':
            self.click(self.brand_manage)
            return BrandManagePage()
