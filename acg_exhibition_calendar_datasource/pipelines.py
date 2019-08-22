# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from acg_exhibition_calendar_datasource.helpers import DBHelper, SettingsHelper
from acg_exhibition_calendar_datasource.models import Exhibition


class AcgExhibitionCalendarDatasourcePipeline(object):
    def __init__(self):
        self.session = DBHelper().get_session()

    def process_item(self, item, spider):
        self.session.add(Exhibition(**item))
        self.session.commit()

    def close_spider(self, spider):
        self.session.close()
