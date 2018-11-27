# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
from sqlalchemy.orm import sessionmaker
from LagouInf.models import Lagouinf

class LagouinfPipeline(object):
    def process_item(self, item, spider):

        return item

    def open_spider(self,spider):
        Session=sessionmaker(bind=engine)
        self=session=Session()

    def close_spider(slef,spider):
        self.session.commit()
        self.session.close()
