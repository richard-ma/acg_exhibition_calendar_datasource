# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AcgExhibitionCalendarDatasourceItem(scrapy.Item):
    # define the fields for your item here like:
    source = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    start_time = scrapy.Field()
    end_time= scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    url = scrapy.Field()
    required_number = scrapy.Field()
    check_id = scrapy.Field()
