#fenci.py
import jieba
import os
import urllib2,re

seg_list=open(r'C:/Python27/context1.csv')
seg=seg_list.read()
re_h=re.compile('</?\w+[^>]*>')
s=re_h.sub('',seg)
fenci=file('fenci1.csv','w')
a=jieba.cut(seg,cut_all=False)
b=' '.join(a)
#print  b
fenci.write(b.encode('gbk'))
