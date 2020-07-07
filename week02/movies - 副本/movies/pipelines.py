# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import pymysql

class MySQLPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME','test')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '123456')

        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    
    #插入数据
    def insert_db(self, item):
        keys = (
            item['name'],
            item['score'],
            item['description'],
            item['releasetime'],
        )
        print(keys)
        try:
            sql = 'INSERT INTO moviesinfo (name, score, description, releasetime) VALUES (%s,%s,%s,%s)'        
            self.db_cur.execute(sql, keys)
            self.db_conn.commit()
            print("Insert finished")
        except:
            print('Insert failed')
            self.db_conn.commit()
            self.db_conn.close()   



