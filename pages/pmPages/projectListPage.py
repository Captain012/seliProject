# projectList
from common.basePage import BasePage
class ProjectListPage(BasePage):
    def get_first_project_name(self):
        return self.get_element_text(self.first_project_name)

    def return_to_home(self):
        self.click(self.home_btn)

