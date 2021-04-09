# _*_ coding: utf-8 _*_
import scrapy
from bs4 import BeautifulSoup
from doubanbook.items import DoubanbookItem

class DoubanSpider(scrapy.Spider):
    # 定义爬虫
    name = 'douban'
    allowed_domains = ['book.douban.com']
    # 起始URL列表
    start_urls = ['http://book.douban.com/top250']


    # 启动爬虫时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象(Request)。
    # startrequests()方法读取start_urls列表中的URL并生成requests对象，发送给引擎。
    # 引擎在指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0,10):
            url = f'https://book.douban.com/top250?start={i*25}'
            yield scrapy.Request(url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎会将下载好的页面(Request对象)发送给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不适用parse作为默认回调参数

    # 解析函数
    def parse(self, response):
        # pass
        # debug
        # items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class':'pl2'})
        for i in range(len(title_list)):
            # 在items.py定义
            item = DoubanbookItem()
            title = title_list[i].find('a').get('title')
            link = title_list[i].find('a').get('href')
            item['title'] = title
            item['link'] = link
            # debug
            # items.append(item)
        # return items
            # 一个parse函数可能获取不到我们想要的所有字段,所有yield后面在发起一个请求，使用parse2取得书的内容
            yield scrapy.Request(url=link, meta={'item': item},callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div',attrs={'class': 'intro'}).get_text
        item['content'] = content
        yield item # 要获取的字段都全了，就可以返回了
