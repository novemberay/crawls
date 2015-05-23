#cleancontents.py
import os
import urllib
import urllib2
import re

fout = open(r'context.csv')
re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #CDATA
re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
re_br = re.compile('<br\s*?/?>',re.I)#<br>
re_blankline = re.compile('\n+')
re_space = re.compile(' ')
re_link = re.compile('http://.*?(.*?).*?.(.*?).html',re.I)
re_tab = re.compile('	')
re_h = re.compile('</?\w+[^>]*>',re.I)#HTML tag
re_comment = re.compile('<!--[^>]*-->')
re_entities = re.compile('&.*?(.*?).*?;')


s = fout.read()
s = re_cdata.sub('',s)#remove CDATA
s = re_script.sub('',s) #remove SCRIPT
s = re_style.sub('',s)#remove style
s = re_br.sub('',s)#remove </br>
s = re_blankline.sub('',s)
s = re_space('',s)
s = re_link('',s)
s = re_tab('',s)
s = re_h.sub('',s) #remove html
s = re_comment.sub('',s)
s = re_entities('',s)
fin = open('content.txt','w')
fin.write(s)
fout.close()

