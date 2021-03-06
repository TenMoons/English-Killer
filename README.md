# 基于Python的英语学习辅助软件
2019-2020 AHU Python课设
***
## 选题背景和依据
*    英语是程序员无法回避的一道门槛，其重要性体现在学习和工作的方方面面。作为计算机相关专业的一名大学生，我认为通过英语六级考试是很有必要的，但是周围很多同学未能通过或者分数很不理想，据此我设想了软件的第一个功能：辅助六级考试。通过分析往年的六级真题试卷，统计出高频词汇，分析一下六级究竟难在哪里。

*    除了考试，还设计了一个针对科研的功能：分析CVPR等顶会文章，统计出高频词汇，帮助我们在入门科研研读论文时更加得心应手。
***
## 分析、开发和测试
### 分析
*    从网络上下载的六级真题试卷文档格式并不统一，有的是.doc格式，而有的是.docx格式。为了便于处理，首先人为地将所有.doc格式文档转换为.docx格式文档，再调用docx库的Document直接对.docx文件进行处理。首先读取文档的内容，然后进行分词，将结果写入txt文件，所有文件读取结束后再读取txt文件进行统计，将结果写入csv文件，并进行降序排列。然后对csv中的数据进行可视化处理，调用pyecharts或者matplotlib库进行操作即可。对于.pdf格式的论文，由于格式的特殊性，故需要先调用处理pdf文件的库pdfminer来读取文件内容，才能进行同六级真题类似的统计分析操作。

### 开发
*    首先根据文件夹的路径遍历文件夹中的文件，如果是.docx类型的文件（对于CVPR论文的解析则是.pdf格式），则读取该文件，遍历文件的每一个段落，然后按照单词的正则表达式进行单词的划分和提取，将得到的单词写入result_test.txt文件。需要注意的是，有很多比较简单的词汇是出现频率极高的，如各种代词、冠词、简单介词、还有一些选项信息等，为了避免它们干扰统计结果，需要建立一个列表exclude_list用于存放这些需要被过滤掉的单词。所有文件都读取结束后，再读取存放了所有试卷出现单词的result_test_txt文件，读取单词信息，并统计每个单词的频率，用一个列表voca来存放单词，注意读取时去掉重复的单词。为了进一步进行筛选，只有当单词长度大于3时，才算作有效单词，将它和它的词频写入word_data.csv文件。全部单词写入完成后，对该csv文件进行排序，按词频降序排列，词频相同则按单词字典序排列。

*    统计结束后，再读取csv文件，分析数据并进行可视化处理，我设计了两种处理方式，一是统计词频的分布区间，二是显示出现频率最高的20或30个单词，通过pyecharts库的函数可以直观地得到数据可视化图，默认保存为html。

### 测试
*    测试数据均从网络获取，其中六级真题数据为2016年6月至2019年6月期间的21套真题，CVPR论文数据来源于CVPR 2019 Best paper Finalist的45篇论文。
测试结果分别为result_test.txt, result_test.csv, pdf_data.txt, pdf_data.csv。六级真题的可视化结果为0.html和1.html，CVPR论文则为3.html和4.html，分别为柱状图和饼状图。

*    从测试结果可以看出，近年来六级真题中出现的词汇，重复度并不高，虽然进行了简单的筛选和过滤处理，但是最后的高频词汇仍然是常用的词汇，CVPR论文的数据也是如此，从柱状图中可以看出词频在[1,3]这一区间的单词占主体，可能这也是六级考试难度较大和论文并不容易读的原因，因此单独只看高频词汇不可靠的，备考、科研和学习都需要脚踏实地。
***

## 待改进：
*    大多数高频词汇是常用的简单词汇，虽进行了过滤操作，但从统计结果看，还需进一步考虑怎么剔除这些常见词。

*    爬取有道/百度翻译获取单词的词性、释义，统计信息更丰富
