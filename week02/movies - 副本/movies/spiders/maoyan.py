import scrapy
from movies.items import MoviesItem
from scrapy.selector import Selector
import time


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com']

    #注释默认的parse函数
    #   def parse(self, response):
    #        pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        url = f'https://maoyan.com/board/4'
        yield scrapy.Request(url=url, callback=self.parse,dont_filter=False)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数
    
    time.sleep(5)
    # 解析函数
    def parse(self, response):
        #print(response.url)
        tags = Selector(response=response).xpath('//dd')
        for tag in tags:
            item = MoviesItem()
            name = tag.css('p.name a::text').extract_first().strip()
            link = 'http://maoyan.com'+tag.css('a::attr(href)').extract_first()
            releasetime = tag.css('.releasetime::text').extract_first().strip()
            score = tag.css('i.integer::text').extract_first().strip()
            score += tag.css('i.fraction::text').extract_first().strip()       
            item['name'] = name
            item['releasetime'] = releasetime
            item['score'] = score
            #print('zheshi',link)
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
    
    #print('时间停留')
    time.sleep(5)
    def parse2(self, response):
        item =response.meta['item']
        description1 = Selector(response=response).css('a.text-link::text').extract()
        #类型转换，list转换成str，方便存储到数据库（list中超过一个值就会报错）
        description = ",".join(description1)
        item['description'] = description
        #print('zheshiyigemiaoshu', description)
        yield item
     