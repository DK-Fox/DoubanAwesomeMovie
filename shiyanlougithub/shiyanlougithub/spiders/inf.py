# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class InfSpider(scrapy.Spider):
    name = 'inf'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for inf in response.css('li.col-12'):
            item=ShiyanlougithubItem()
            item['name']=inf.css('h3 a::text').extract_first().strip(),
            item['update_time']=inf.css('relative-time::text').extract_first()
            
            other_url= response.urljoin(inf.css('h3 a::attr(href)').extract_first())
            request=scrapy.Request(other_url,callback=self.parse_other)
            request.meta['item']=item

            yield request

        next_page=response.css('div.pagination a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page,self.parse)

    def parse_other(self,response):
        item=response.meta['item']
        inf=response.css('ul.numbers-summary li')
        item['commits']=inf[0].css('span::text').extract_first().strip()
        item['branches']=inf[1].css('span::text').extract_first().strip()
        item['releases']=inf[2].css('span::text').extract_first().strip()

        yield item

