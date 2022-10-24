# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixinrenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    iname = scrapy.Field()
    areaName = scrapy.Field()
    cardNum = scrapy.Field()
    caseCode = scrapy.Field()
    courtName = scrapy.Field()
    disruptTypeName = scrapy.Field()

