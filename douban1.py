import requests
from bs4 import BeautifulSoup as bs


# Python 使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
    header = {} # 字典要先定义才能使用，直接使用会报错。
    header['user-agent'] = user_agent

    # url = "https://book.douban.com/top250"

    # response = requests.get(url，headers=header)
    response = requests.get(myurl,headers=header)
    # print(response.text)
    bs_info = bs(response.text, 'html.parser') # lxml语法分析器更强大，兼容性也更强
    # print(bs_info.find_all('div',attrs={'class':'pl2'})[0]) # 不用正则就能找想要的内容,找div下所有匹配attrs
    for tags in bs_info.find_all('div', attrs={'class':'pl2'}):
        # 获取a标签
        # a_tag = tags.contents[1]
        # print(a_tag)
        for atag in tags.find_all('a',):
            # 获取所有连接
            print(atag.get('href'))
            # 获取图书名字
            print(atag.get('title'))
urls = tuple(f'https://book.douban.com/top250?start={ page * 25}' for page in range(10)) # python3.6开始支持f-string
base_url = 'https://book.douban.com/top250?start='
# urls = [base_url + str(i * 25) for i in range(10)]
print(urls)

from time import sleep # 反之被禁爬
if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)