# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShengshiliandongItem(scrapy.Item):
    # define the fields for your item here like:
    first_city = scrapy.Field()
    second_city = scrapy.Field()
    third_city = scrapy.Field()
    fouth_city = scrapy.Field()
    fifth_city = scrapy.Field()
    pass
