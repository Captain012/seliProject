# basemethods
import logging
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config.env import Env
from common.baseDriver import BaseDriver
from utils.handle_path import GetPath
from utils.handle_getYaml import get_yaml_data
class BasePage:
    def __init__(self):
        self.driver = BaseDriver().get_driver()
        self.elements = get_yaml_data(GetPath.config_path/'allElements.yaml')[self.__class__.__name__]
        for elementName,locator in self.elements.items():
            setattr(self,elementName,locator)

    def open_url(self,url):
        self.driver.get(url)
        # print('打开成功')

    def get_element(self,locator,
                     timeout=Env.TIMEOUT,
                     polly_frequency=Env.POLL_FREQUENCY,
                     elements = False):
        # print(type(timeout))
        # print(timeout)
        # print(type(polly_frequency))
        # print(polly_frequency)
        try:
            if not elements:
                return WebDriverWait(self.driver,timeout,polly_frequency).until(EC.visibility_of_element_located(locator))
            else:
                return WebDriverWait(self.driver,timeout,polly_frequency).until(EC.visibility_of_all_elements_located(locator))
        except:
            error_name = list(self.elements.keys())[list(self.elements.values()).index(locator)]
            from utils.handle_loguru import log
            log.error(f'未找到该元素:{error_name}')
            pcname = os.path.join(GetPath.screeenshot_path,f'{error_name}未找到.png')
            print(pcname)
            self.driver.save_screenshot(pcname)
            print('图片已保存')
            return False
    def get_element_text(self,locator,elements = False):
        target = self.get_element(locator,elements = elements)
        if not elements:
            return target.text
        else:
            list = []
            for i in target:
                list.append(i.text)
            return list


    #下面重点看用了哪些参数
    def input(self,locator,text,append = False):
        if append == False:
            self.get_element(locator).clear()
            self.get_element(locator).send_keys(text)
        if append == True:
            self.get_element(locator).send_keys(text)

    def click(self,locator):
        self.get_element(locator).click()


    def is_element(self,locator):
        if self.get_element(locator):
            return True
        else:
            return False

    def is_this_url(self,url,timeout=Env.TIMEOUT,frenquency = Env.POLL_FREQUENCY):
        return WebDriverWait(self.driver,timeout,frenquency).until(EC.url_to_be(url))

    def quit_browser(self):
        self.driver.quit()





if __name__ == '__main__':
    pass
