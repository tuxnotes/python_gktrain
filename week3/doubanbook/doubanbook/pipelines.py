# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# pipelines.py用于接受爬取后的字段，然后保存
from itemadapter import ItemAdapter


class DoubanbookPipeline:

    def __init__(self):
        self.article = open('./doubanbook.txt','a+',encoding='utf-8')

    # 每一个item管道组件都会都用该方法，并且返回一个item对象实例或raise 
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        content = item['content']
        output = f'{title}\t{link}\t{content}\n\n'
        self.article.write(output)
        self.article.close()

        return item
    # 管道默认没有打开，所以需要改下settings.py
    # 注册在settings.py文件的ITEM_PIPELINES中，激活组件
