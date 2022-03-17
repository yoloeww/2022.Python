# -*- codeing = utf-8 -*-
# @Time : 2022/3/16 23:46
# @Author : yolo
# @File : 2022.3.16.毕业论文数据分析.py
# @Software: PyCharm



import xlsxwriter
import jieba
import pandas as pd
import wordcloud
import numpy as np
from PIL import Image
import os

df = pd.read_excel('146891403_疫情期间盒马鲜生的消费者满意度调查_174cbc86-61ff-4d50-91f0-4230e9d3bbc0.xlsx')
a = df['6、疫情期间，在盒马鲜生网购中，您最在意的点是什么？']
b = df['13、您认为以下总体情况下，以下哪些点盒马鲜生做的很好？']
##词频统计变量
counts = {}

# 统计词频
for word in a:
    counts[word] = counts.get(word, 0) + 1

for word in b:
    counts[word] = counts.get(word, 0) + 1

# 字体
font = r'C:\\Windows\\fonts\\simkai.ttf'
mask = np.array(Image.open('zgdt3.jpg'))

my_wordcloud = wordcloud.WordCloud(max_words=300,  # 最多显示词语数量
                                   min_font_size=1,  # 最小字号
                                   mask=mask,  # 形状
                                   repeat=True,  # 重复显示词语
                                   scale=10,  # 分辨率放大倍数
                                   background_color='white',  # 背景颜色
                                   font_path=font)  # 字体
# 生成词云
my_wordcloud.generate_from_frequencies(counts)
my_wordcloud.to_file('词云.jpg')



