import requests
import lxml.etree

url = 'https://book.douban.com/subject/2035179/'

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
header = {}
header['user-agent']= user_agent
response = requests.get(url, headers=header)
selector = lxml.etree.HTML(response.text)
name = selector.xpath('//*[@id="wrapper"]/h1/span/text()') # 返回的是一个对象，所以需要加text()方法
print(name)

# pandas to csv
mylist = [str(name),'tux',4.5]
columns_name = ['one']

import pandas as pd

book1 = pd.DataFrame(columns=columns_name,data=mylist)
book1.to_csv('./book1.csv',encoding='utf-8')
