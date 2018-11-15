# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class InfSpider(scrapy.Spider):
    name = 'inf'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for inf in response.css('li.col-12'):
            item=ShiyanlougithubItem({
                'name':inf.css('h3 a::text').extract_first().strip(),
                'update_time':inf.css('relative-time::text').extract_first()
            })
            yield item

        next_page=response.css('div.pagination a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page,self.parse)
