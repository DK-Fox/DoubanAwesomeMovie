import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker
from models import DoubanMovie, engine

myfont=matplotlib.font_manager.FontProperties(
    fname='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
)

# while 1
    # pass
IMG_PATH="/app/img/"
sql=r"select * from DoubanMovie;"
df=pd.read_sql_query(sql,engine)

class FromDBDataGenerateIMG(object):
    def generate_pie(self):
        pie1=df.drop('location',axis=1).\
            join(df['location'].str.\
                 split('/',expand=True).\
                 stack().reset_index(level=1,drop=True).\
                 rename('location')).groupby('location').size()
        # 处理“中国大陆”和“香港”
        chn=pie1['中国大陆']+pie1['香港']
        pie1=pie1.drop(['中国大陆','香港'])
        pie1['中国']=chn

        # 处理大量的其他国家
        rate=pie1/pie1.sum()<0.05
        other=pie1[rate].sum()
        pie1=pie1[~rate]
        pie1['其他']=other

        fig1,ax1=plt.subplots()
        ax1.pie(pie1,labels=pie1.index,autopct='%1.1f%%',shadow=True,startangle=90)
        ax1.axis('equal')
        ax1.set_title(u'测试',FontProperties=myfont)
        fig1.savefig(IMG_PATH+'pie.png')

    def generate_plot(self):
        plot1=df.groupby('year').size()
        print(plot1)

    def generate_barh(self):
        barh1=df.drop('type',axis=1).\
                join(df['type'].str.\
                    split('/',expand=True).\
                    stack().reset_index(level=1,drop=True).\
                    rename('type')).groupby('type').size()
        print(barh1)


if __name__=='__main__':
    test=FromDBDataGenerateIMG()
    test.generate_pie()
    test.generate_plot()
    test.generate_barh()
