# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class KanxuePipeline(object):
    def __init__(self):
        f = open('essence.csv','w',encoding='utf-8')
        firstRow = [
            'title','rank',
            'username','upDate','eyeNum','commentNum'
        ]
        self.writer = csv.DictWriter(f,fieldnames=firstRow)
        self.writer.writeheader()
    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
