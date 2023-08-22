# basebrowser
from config.env import Env
from selenium import webdriver
class singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance



class BaseDriver(singleton):
    driver = None
    def get_driver(self,browser_type = Env.BROWSER,headless_flag=Env.HEADLESS_FLAG):
        if self.driver is None:  # 参考单例的第二种实现；结合下面的test_flag 123
            if not headless_flag:  # 如果是有头
                if browser_type == 'firefox':  # 判断浏览器类型 打开对应的浏览器
                    self.driver = webdriver.Firefox()
                elif browser_type == 'chrome':
                    self.driver = webdriver.Chrome()

            else:
                if browser_type == 'firefox':
                    option = webdriver.FirefoxOptions()
                    option.add_argument('--headless')
                    self.driver = webdriver.Firefox(options=option)
                elif browser_type == 'chrome':
                    option = webdriver.ChromeOptions()
                    option.add_argument('--headless')
                    self.driver = webdriver.Chrome(options=option)

            self.driver.maximize_window()
            self.driver.set_page_load_timeout(Env.PAGE_LOAD_TIMEOUT)  # 加载页面的最大超时时间
        return self.driver





