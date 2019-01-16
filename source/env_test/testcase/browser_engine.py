import configparser
import os
from selenium import webdriver
from source.env_test.testcase import Logger

mylogger = Logger(logger='TestMyLog').getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    firefox_driver_path = dir + '/tools/geckodriver.exe'
    chrome_driver_path = dir + '/tools/chromedriver.exe'

    def open_browser(self):
        # 读取配置文件
        config = configparser.ConfigParser()
        file_path = self.dir + '/config/config.ini'
        print('file_path===========', file_path)
        config.read(file_path)
        # 从配置 文件 中获取浏览器名称并打印日志
        browser = config.get('browserType', 'browserName')
        print('browser=========', browser)
        mylogger.info('you had select %s' % browser)
        # 从配置文件 中获取要访问的URL并打印日志
        url = config.get('testServer', 'URL')
        print('url=============', url)
        mylogger.info('you want to visit %s' % url)
        if browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
            mylogger.info('Starting firefox browser')
        elif browser == 'Chrome':
            self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
            mylogger.info('Starting chrome browser')
        # URL请求
        self.driver.get(url)
        mylogger.info('Open url: %s' % url)
        # 窗口全屏幕
        self.driver.maximize_window()
        mylogger.info('Maximize the current window')
        # 加载等待时间
        self.driver.implicitly_wait(5)
        mylogger.info('Set implicitly wait 10 seconds')
        return self.driver

    def quit_browser(self):
        mylogger.info('Now,Close and quit the browser')
        self.driver.quit()
