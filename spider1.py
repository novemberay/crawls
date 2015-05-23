# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

filename = "spider1V1.txt"
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
headers = {'user_agent':user_agent}
f = open("spider1V1.txt","w")
for i in range(3):
    url = 'http://jwc.ccnu.edu.cn/sublist.aspx?id=ca000103&page='+str(i+1)
    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<tr>.*?<td.*?td.*?<a.*?>(.*?)</a>.*?</tr>',re.S)
        items = re.findall(pattern,content)
        for item in items:
            f.write(item.encode('gbk'))
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason