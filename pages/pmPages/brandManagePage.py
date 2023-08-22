# brandManagePage
from common.basePage import BasePage
from time import sleep
class BrandManagePage(BasePage):
    def query_list(self,stuff):
        self.input(self.search_box,stuff)
        self.click(self.search_btn)

    def get_name_list(self):
        sleep(1)
        return self.get_element_text(self.name_list,elements=True)

    def return_to_home(self):
        self.click(self.home_btn)


