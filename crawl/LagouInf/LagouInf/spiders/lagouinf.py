# -*- coding: utf-8 -*-
import scrapy


class LagouinfSpider(scrapy.Spider):
    name = 'lagouinf'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    def parse(self, response):
        pass
