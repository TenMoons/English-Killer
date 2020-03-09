# coding = utf-8

from docx import Document
import os, re, csv
import pandas as pd


'''
准备工作：读取所有试卷中的单词，全部存入result_test.txt中
'''
words=[]  # 存放所有单词的列表

# 收集一些需要被筛选的词汇
exclude_list = [
        # 代词
        'i', 'you', 'he', 'she', 'it', 'we', 'they', # 主格
        'me', 'him', 'her', 'us', 'them', # 宾格
        'my', 'your', 'his', 'her', 'its', 'our', 'their', # 形容词性
        'mine', 'yours', 'his', 'hers', 'ours', 'yours', 'theirs',  # 名词性
        'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves', # 反身代词
        'this', 'that', 'such', 'these', 'those', 'some',
         'who', 'whom', 'whose', 'which', 'what', 'whoever', 'whichever', 'whatever', 'when',
         'as', 'self',
         'one', 'some', 'any', 'each', 'every', 'none', 'no', 'many', 'much', 'few', 'little',
         'other', 'another', 'all', 'both', 'neither', 'either',
         # 冠词
         'a', 'an', 'the',

         # 简单介词
         'about', 'with',
         'into', 'out', 'of' , 'without',
         'at', 'in', 'on', 'by', 'to',

         # 简单连词
         'and', 'also', 'too','not', 'but',

         # 简单量词
         'one', 'two', 'three', 'four', 'five',
         # 简单动词
         'is', 'am', 'are', 'was', 'were', 'be',

         # 选项
         'a', 'b', 'c', 'd',
         # 其他
         'or', 'if', 'else', 'for','have', 'must', 'has', 'new', 'time',

]

# 判断文件后缀,只读取.docx格式的文件
def isDocx(s, *endString):
    array = map(s.endswith, endString)
    if True in array:
        return True
    else:
        return False

# 从文件夹中批量读取文件,path是文件路径
def readFile(path):
    fileList = os.listdir(path)
    for filename in fileList:
        # 先判断文件格式
        if isDocx(filename, '.docx'):
            # 建立文件绝对路径
            filepath = path + '/' + filename
            # 根据绝对路径读取文件
            paper = Document(filepath)
            # 解析文件内容
            parseFile(paper)


# 解析文件
def parseFile(file):
    # 存放统计结果
    global words
    output = open('result_test.txt', 'a+', encoding='utf-8')
    article = ''
    # 遍历试卷的每一段,将试卷转换为字符串
    for value in file.paragraphs:  # str:value.text
        article += value.text
    article = article.lower()  # 全部转换为小写形式
    words = re.compile(r'[a-zA-Z]+', re.A).findall(article)   # 通过正则表达式进行单词匹配
    for i in words:
        if i in exclude_list:  # 将需要移除的单词从列表中删除
            words.remove(i)
        else:
            output.write(i)
            output.write(' ')

'''
统计分析：对上一阶段的txt文件进行统计和分析，计算每个单词出现的次数，写入csv文件
'''
def analysis():
    # 从txt文件中读取单词并转换为列表
    f = open('result_test.txt')
    voca = f.read().split(' ')
    f.close()

    # 打开csv文件,并写入
    csv_file = open('word_data.csv', 'w', newline='')
    csv_write = csv.writer(csv_file)
    csv_write.writerow(['单词','词频' ])
    # print(voca)
    while len(voca) is not 0:
        word = voca[0]
        cnt = 0
        while word in voca:  # 计算单词w的出现次数
            voca.remove(word)  # 删除已经统计过的单词
            cnt += 1
        if(len(word) > 3):
            csv_write.writerow([word, cnt])  # 写入csv文件
    csv_file.close()

# 根据词频进行排序，同样词频则按字幕序
def sortTime():
    df = pd.read_csv('word_data.csv', encoding='utf-8_sig')
    df = df.sort_values(['词频', '单词'], ascending=False)
    # print(df)
    df.to_csv('word_data.csv', header=True, index=False, encoding='utf-8_sig')


'''
对数据进行可视化处理
'''
# Bar_gui.py
# Pie_gui.py


if __name__ == '__main__':
    path = 'cet6'  # 存放试卷文件的文件夹路径
    readFile(path)
    analysis()
    sortTime()



