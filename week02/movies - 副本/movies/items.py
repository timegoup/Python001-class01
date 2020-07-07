# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    #电影名称
    name = scrapy.Field()
    #电影类型
    description = scrapy.Field()
    #电影上映时间
    releasetime = scrapy.Field()
    #电影评分
    score = scrapy.Field()
    


    
