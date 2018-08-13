# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import MySQLdb.cursors
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
import logging

class StfPipeline(object):
    def process_item(self, item, spider):
        return item

class JurisPipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLStorePipeline(object):
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def __init__(self, stats):
        #Instantiate DB
        self.conn = MySQLdb.connect(user='root', passwd='121294', db='stf', host='127.0.0.1', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        self.logger = logging.getLogger()


    def process_item(self, item, spider):       
        
        self.cursor.execute("SELECT * FROM processos WHERE data=%s AND observacao=%s" , (item['data'],item['observacao'],))

        processo = self.cursor.fetchone()

        if not processo:         
            self.cursor.execute("""INSERT INTO processos (data,andamento,observacao) VALUES (%s,%s,%s)""", (item['data'],item['andamento'],item['observacao']))
            self.conn.commit()
            self.logger.info('Inserindo no BD')      
        else:
            self.logger.info('Já existe esse andamento na base de dados')      