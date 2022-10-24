# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import MySQLdb
class ShixinrenPipeline:
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost',
                               user='root',
                               passwd='123456',
                               db='crawler',
                               port=3306)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into sxr VALUES (%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql,(item['iname'],item['areaName'],item['cardNum'],item['caseCode'],item['courtName'],item['disruptTypeName']))
        self.conn.commit()
        print(item['iname'])
        return item
