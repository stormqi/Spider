# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:
    position = name = scrapy.Field()
    position_link = name = scrapy.Field()
    position_type = name = scrapy.Field()
    people_num = name = scrapy.Field()
    work_location = name = scrapy.Field()
    publish_time = name = scrapy.Field()
