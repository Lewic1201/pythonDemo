# coding=utf-8
import time
import unittest
from source.envTest.testcase import BrowserEngine


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        # 得到driver
        browser = BrowserEngine()
        self.driver = browser.open_browser()
        print(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print('Test Pass')
        except Exception as e:
            print('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()
