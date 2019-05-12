# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class CartTripPipeline(object):
    def process_item(self, item, spider):
        return item

class CartTripPipelineMongo(object):
    client=None
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(host='127.0.0.1',port=27017)
        self.db=self.client['test']

    def process_item(self,item,spider):
        collection = self.db['cart_trip']
        item_dic=dict(item)
        collection.insert(item_dic)

        return item

    def close_spider(self,spider):
        self.client.close()