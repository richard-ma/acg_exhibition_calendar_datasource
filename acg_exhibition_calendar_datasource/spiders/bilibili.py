# -*- coding: utf-8 -*-
import scrapy
import json
from acg_exhibition_calendar_datasource.items import AcgExhibitionCalendarDatasourceItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']

    def __init__(self):
        self.start_page = 1
        self.start_urls = [self.next_page_url()]

    def next_page_url(self, num=0):
        self.start_page = num + 1
        return 'https://show.bilibili.com/api/ticket/project/listV2?page=%d&pagesize=20&area=-1&platform=web&p_type=全部类型' % (self.start_page)

    def parse(self, response):
        data = json.loads(response.text)

        if data['errno'] != 0:
            return False # ERROR! STOP Crawling

        for d in data['data']['result']:
            item = AcgExhibitionCalendarDatasourceItem()
            item['source'] = BilibiliSpider.name
            item['code'] = d['id']
            item['name'] = d['project_name']
            item['address'] = d['venue_name']
            item['city'] = d['city_name']
            item['url'] = d['url']

            item['start_time'] = d['start_time']
            start_time = d['start_time'].split('.')
            end_time = d['end_time'].split('.')
            print(start_time)
            print(end_time)
            if len(end_time) == 2:
                if int(end_time[0]) < int(start_time[1]):
                    result_end_time = str(int(start_time[0])+1) + '.' + d['end_time']
                else:
                    result_end_time = str(int(start_time[0])) + '.' + d['end_time']
            else:
                result_end_time = d['end_time']
            item['end_time'] = result_end_time

            yield item

        total_pages = data['data']['numPages']
        if self.start_page < total_pages:
            url = self.next_page_url(self.start_page)
            yield scrapy.Request(url, callback=self.parse)
