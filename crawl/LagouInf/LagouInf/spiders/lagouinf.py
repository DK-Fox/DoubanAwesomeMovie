# -*- coding: utf-8 -*-
import scrapy


class LagouinfSpider(scrapy.Spider):
    name = 'lagouinf'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/']

    def parse(self, response):
        '''
        Get login page
        '''
        login_page=response.css('g_tbar div.lg_tbar_l a::attr("href")').extract_first()
        yield response.follow(login_page,self.login_parse)

    def login_parse(self,reponse):
        '''
        Log in
        '''

    def after_login_parse(self,response):
        '''
        Start to get information
        '''

