# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class BollywoodPipeline(object):

    def __init__(self):
        #Creates a connection
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        #Creates a database
        db = self.conn['celebs']

        #Creating a connection
        self.collection = db['celeb_details']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
