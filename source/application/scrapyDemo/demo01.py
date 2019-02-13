# https://www.makcyun.top/web_scraping_withpython2.html

import pandas as pd
import csv
import os


def simple_scrapy(baseUrl, pageNum, saveFile='test.csv'):
    for i in range(1, pageNum + 1):  # 爬取每页数据
        url = baseUrl % (str(i)) if pageNum != 1 else baseUrl
        tb = pd.read_html(url)[0]  # 经观察发现所需表格是网页中第4个表格，故为[3]

        tmp = saveFile
        suffix = 1
        while os.path.exists(tmp):
            suffix += 1
            tmp = saveFile[:4] + str(suffix) + saveFile[4:]

        tb.to_csv(tmp, mode='a', encoding='utf-8', header=1, index=0)
        print('第' + str(i) + '页抓取完成')


if __name__ == '__main__':
    url1 = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s'
    url2 = 'http://ranking.promisingedu.com/qs'

    # simple_scrapy(url1, 177)
    simple_scrapy(url2, 1)
