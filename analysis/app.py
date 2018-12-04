import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker
from models import DoubanMovie, engine
#处理中文字体的方法
from matplotlib.font_manager import _rebuild

_rebuild()
mpl.rcParams['font.sans-serif']=u'SimHei'
#------------------

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
        fig1.savefig(IMG_PATH+'pie.png')

    def generate_plot(self):
        plot1=df.groupby('year').size()
        fig2,ax2=plt.subplots()
        ax2.plot(plot1.index,plot1)
        fig2.savefig(IMG_PATH+'plot.png')

    def generate_barh(self):
        barh1=df.drop('type',axis=1).\
                join(df['type'].str.\
                    split('/',expand=True).\
                    stack().reset_index(level=1,drop=True).\
                    rename('type')).groupby('type').size()
        barh1=barh1.drop('官方网站:')
        rate=barh1/barh1.sum()<0.05
        other=barh1[rate].sum()
        barh1=barh1[~rate]
        barh1['其他']=other
        print(barh1)

        y_pos = np.arange(len(barh1))
        print(y_pos)
        print(list(barh1.index))
        fig3,ax3=plt.subplots()
        ax3.barh(y_pos,barh1,align="center",color='green',ecolor='black')
        ax3.set_yticks(y_pos)
        ax3.set_yticklabels(barh1.index)
        ax3.invert_yaxis()
        fig3.savefig(IMG_PATH+'barh.png')

if __name__=='__main__':
    test=FromDBDataGenerateIMG()
    test.generate_pie()
    test.generate_plot()
    test.generate_barh()
