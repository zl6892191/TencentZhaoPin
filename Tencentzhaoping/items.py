# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentzhaopingItem(scrapy.Item):
    name = scrapy.Field()
    categroy = scrapy.Field()
    people = scrapy.Field()
    address = scrapy.Field()
    datetime = scrapy.Field()
