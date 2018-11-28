# -*- coding: utf-8 -*-

import scrapy
from douban_movie.items import MovieItem
import logging

class AwesomeMovieSpider(scrapy.Spider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    # start_urls=['https://movie.douban.com/subject/27615441/']
    start_urls = ('https://movie.douban.com/subject/{}/'.format(x) for x in range(10000000))

    def parse(self, response):
        item=MovieItem()
        item['url']=response.url
        item['name']=response.css('h1 span::text').extract_first().strip()
        item['year']=response.css('h1 .year::text').extract_first().strip()[1:-1]
        infos=response.css('div#info span::text').extract()
        for index,info in enumerate(infos):
            if info=='类型:':
                break
        infos=infos[index+1:]
        for index,info in enumerate(infos):
            if info=='制片国家/地区:':
                break
        infos=infos[:index]
        item['type']='/'.join(infos)
        infos=response.css('div#info::text').extract()
        for info in infos:
            i=info.strip().strip('/')
            if i:
                item['location']=i.replace(' ','')
                break
        item['summary']=response.css('div.related-info div.indent span::text').extract_first().strip().replace(' ','')
        item['score']=response.css('strong.rating_num::text').extract_first().strip()
        yield item
