import csv
import importlib
import sys
import pandas as pd

importlib.reload(sys)

import os.path
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


# text_path = r'photo-words.pdf'

# 判断文件后缀,只读取.pdf格式的文件
def isPdf(s, *endString):
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
        if isPdf(filename, '.pdf'):
            # 建立文件绝对路径
            filepath = path + '/' + filename
            parse(filepath)

def parse(filepath):
    '''解析PDF文本，并保存到TXT文件中'''
    fp = open(filepath, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page内容
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(r'pdf_data.txt', 'a', encoding='utf-8_sig') as f:
                        results = x.get_text()
                        f.write(results + "\n")
'''
统计分析：对上一阶段的txt文件进行统计和分析，计算每个单词出现的次数，写入csv文件
'''
def analysis():
    # 从txt文件中读取单词并转换为列表
    f = open('pdf_data.txt', encoding='utf-8_sig')
    voca = f.read().split(' ')
    f.close()

    # 打开csv文件,并写入
    csv_file = open('pdf_data.csv', 'w', newline='', encoding='utf-8_sig')
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
    df = pd.read_csv('pdf_data.csv', encoding='utf-8_sig')
    df = df.sort_values(['词频', '单词'], ascending=False)
    # print(df)
    df.to_csv('pdf_data.csv', header=True, index=False, encoding='utf-8_sig')


if __name__ == '__main__':
    path = 'paper'  # 存放论文文件的文件夹路径
    readFile(path)
    analysis()
    sortTime()


