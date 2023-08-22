# conftest
import pytest
from pages.loginPage import Login
from time import sleep
@pytest.fixture(scope='session',autouse=False)
def auto_login():
    print('自动化测试开始---尝试登录中...')
    main_page = Login().get_login_page()
    yield main_page.login('松勤老师','123456')
    main_page.quit_browser()
    print('登录成功')

# @pytest.fixture(scope='class',autouse=False)
# def quit_browser():
#     page = Login()
#     yield
#     page.quit_browser()
#     sleep(3)





def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

