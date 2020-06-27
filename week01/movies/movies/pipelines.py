# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class MoviesPipeline:
    #def process_item(self, item, spider):
        #return item
    def process_item(self, item, spider):
        name = item['name']
        score = item['score']
        description = item['description']
        releasetime = item['releasetime']
        output = f'|{name}|\t|{description}|\t|{releasetime}|\t|{score}|\n\n'
        #苹果电脑 encoding='utf-8'
        with open('./maoyanmovie.csv', 'a+', encoding='gbk') as article:
            article.write(output)
        return item
