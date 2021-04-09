# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# items.py中定义要抓取的内容，如下面的title link content

# title 'div',class_='pl2' > a['title']
# link 'div',class_='pl2' > a['href']
# content 'div',class='intro' > text

class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field() # Field()统一转换成字符创
    link = scrapy.Field()
    content = scrapy.Field()
