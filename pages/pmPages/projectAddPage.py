# projectAddPage
from common.basePage import BasePage


class ProjectAddPage(BasePage):
    def add_project(self,idx_class1,idx_class2,pjname,pjtitle,idx_brand):
        self.click(self.project_class_select)  #商品分类按钮
        self.project_class_select_idx1[-1] = self.project_class_select_idx1[-1].format(idx_class1)
        self.click(self.project_class_select_idx1) #商品分类一级
        self.project_class_select_idx2[-1] = self.project_class_select_idx2[-1].format(idx_class2)
        self.click(self.project_class_select_idx2) #商品分类二级
        self.input(self.product_name,pjname)
        self.input(self.product_subtitle,pjtitle)
        self.click(self.brand_select)
        self.brand_select_idx[-1] = self.brand_select_idx[-1].format(idx_brand)
        self.click(self.brand_select_idx)
        self.click(self.next_to_promotion_btn)
        self.click(self.next_product_attribute_btn)
        self.click(self.next_product_related_btn)
        self.click(self.complete_btn)
        self.click(self.submit_btn)
    def return_to_home(self):
        self.click(self.home_btn)



