# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KanxueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rank = scrapy.Field()
    username = scrapy.Field()
    upDate = scrapy.Field()
    eyeNum = scrapy.Field()
    commentNum = scrapy.Field()
    pass
