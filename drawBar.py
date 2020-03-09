# coding = utf-8

'''
统计每个词频阶段的单词数量
'''

import pandas as pd
import csv
from pyecharts import Bar

# 统计词频分布,绘制成柱状图
def drawBarByTimes(file):
    pr = pd.read_csv(file,encoding='utf-8_sig')
    times = []
    for i in pr['词频']:
        times.append(int(i))
    times1=[]
    times2=[]
    times3=[]
    times4=[]
    times5=[]
    times6=[]
    times7=[]
    times8=[]
    times9=[]
    for i in times:
        if i == 1:
            times1.append(i)
        elif i == 2:
            times2.append(i)
        elif i == 3:
            times3.append(i)
        elif i == 4:
            times4.append(i)
        elif i == 5:
            times5.append(i)
        elif 5<i<=20:
            times6.append(i)
        elif 20<i<=60:
            times7.append(i)
        elif 60<i<=100:
            times8.append(i)
        else:
            times9.append(i)

    index=['1','2','3','4','5','5~20','20~60','60~100','>=100']
    values=[len(times1), len(times2),len(times3),len(times4),len(times5), len(times6), len(times7), len(times8), len(times9)]
    #plt.bar(index,values)
    #plt.show()
    bar = Bar("词频区间分布")
    bar.add("词频", index, values, mark_line=['average'], mark_point=['max','min'])
    bar.render()

#drawBarByTimes('word_data.csv')
drawBarByTimes('pdf_data.csv')


