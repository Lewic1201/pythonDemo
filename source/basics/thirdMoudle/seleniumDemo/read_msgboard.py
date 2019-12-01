import re
from selenium import webdriver

browser = webdriver.Chrome()

# 打开百度网页
browser.get('http://127.0.0.1:5002/message')
# browser.set_window_size(480, 800)

# link = browser.find_elements_by_tag_name("a")[0].click()


strs = '''需求：现在有一个网站的页面，我希望用python自动化的测试点击这个页面上所有的在本窗口跳转，并且是本站内的链接，前往到链接页面之后在通过后退返回到原始页面。
　　要完成这个需求就必须实现3点：
　　1. 找到原始页面上面所有的在本窗口内跳转的链接
　　2. 跳转到目标页面之后，“后退”到原始页面
　　3. 在原始页面上继续点击后续的链接
　　首先，要找到页面上的所有链接并不困难。selenium为我们提供了find_elements_by_tag_name方法。我们只需要在初始化webdriver之后，调用
　　driver.find_elements_by_tag_name("a")
　　就能找到页面上的所有a标签。
　　我们可以对所有的a标签进行点击，但是这样的话我们不能保证所有的a标签所指向的目标页面都是站内的，有可能目标是其他的站外网页；另外这样也不能保证该跳转页面是在本窗口跳转而不是新开一个窗口。
　　解决办法：
　　使用selenium.webdriver.remote.webelement.WebElement提供的get_attribute方法。
　　通过get_attribute拿到该a标签的各种属性，通过判断找到符合要求的元素进行点击。
　　get_attribute("href") 得到a标签对应的目标页面的URL，对URL进行判断就可以了解到该页面是否站内页面。我们可以知道，如果是站内页面的话这个属性一般会是一个相对路径,或者包含了本站域名，但如果是站外页面的话，那它一定是包含了“http”的一个url。
　　get_attribute("target")如果target不是"_blank"的话，可以判断该页面是在本窗口跳转的。
　　跳转到下一页面后如何返回原始页面呢？
　　selenium webdriver 提供了back方法可以轻松的达到这个目标：driver.back()
　　最后，需要在返回了原始页面之后继续点击下一个链接进行测试，这个不用说肯定要使用for loop：
　　for i in range(0, len(driver.find_elements_by_tag_name("a"))):
　　在python中，如果我们指定i在range(0, x)中循环时，会以1为步长来遍历从0到(x-1)的序列。例如：range(0,5)会得到[0, 1, 2, 3, 4]。当我们想更改range的步长时，则需要为range方法提供第三个参数。例如：range(0,5,2)，则会以2为步长，得到[0,2,4]这个序列。
　　另外，我们也可以使用类似C#中foreach的方法：
　　for targetLink in driver.find_elements_by_tag_name("a")：
　　这种方法同样可以遍历所有的a标签集合中的所有元素。
　　如果使用第二种方法，我们觉得这个需求可以简单的实现为：'''

for i in range(100):
    username = browser.find_element_by_name("username")
    context = browser.find_element_by_name("context")
    sub = browser.find_elements_by_id('sub')[0]

    username.send_keys("lewic" + str(i))

    send_ls = re.split(u'[,:.，。"]', strs)
    context.send_keys(send_ls[i % len(send_ls)])
    sub.submit()

browser.quit()
