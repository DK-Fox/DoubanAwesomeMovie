# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from douban_movie.models import DoubanMovie, engine


class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        item['score']=float(item['score'])
        item['year']=int(item['year'])
        self.session.add(DoubanMovie(**item))
        return item

    def open_spider(self, spider):
        Session=sessionmaker(bind=engine)
        self.session=Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
