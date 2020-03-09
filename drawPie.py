# coding = utf-8

'''
统计每个词频阶段的单词数量
'''

import pandas as pd
import csv
from pyecharts import Pie

# 将词频最高的length个单词，绘制成饼状图
def drawPieByTimes(file,length):
    pr = pd.read_csv(file, nrows=length, encoding='utf-8_sig')
    labels = []
    cnt = []    # 饼状图的标签
    for i in pr['单词']:
        labels.append(i)
    for i in pr['词频']:
        cnt.append(int(i))
    #print(labels)
    #print(cnt)
    pie = Pie('高频词汇一览', '词频最高的单词', title_pos='center')
    pie.add('词频', labels, cnt, is_legend_show=False)
    pie.render()

#drawPieByTimes('word_data.csv',20)
drawPieByTimes('pdf_data.csv', 30)

