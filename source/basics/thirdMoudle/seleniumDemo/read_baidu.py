from selenium import webdriver

browser = webdriver.Chrome()

# 打开百度网页
browser.get('http://www.baidu.com')
# browser.set_window_size(480, 800)

# 百度搜索
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
# browser.quit()
