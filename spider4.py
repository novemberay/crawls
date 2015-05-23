#spider4  extract html of CCCU news
import urllib
import urllib2
from sgmllib import SGMLParser
import re
import os

def getHTML(url):
	page = urllib.urlopen(url)
	html = page.read()
	page.close()
	return html

class URLParcer(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []

	def start_a(self,attrs):
		href = [v for k,v in attrs if k=='href']
		if href:
			self.urls.extend(href)

reg = '/xin/dangzhengxinwen/20.*'
IParser = URLParcer()
f = file('context.csv','w')
for i in range(2):
    socket = urllib.urlopen("http://www.ccnu.com.cn/xin/dangzhengxinwen/list_2_"+str(i+1)+".html")# extract news' urls from 1st and 2nd page
    IParser.feed(socket.read())
    pattern = re.compile(reg)
    for url in IParser.urls:
	    if pattern.match(url):
	    	url2="http://www.ccnu.com.cn"+url+"\n"
	    	response = urllib2.urlopen(url2)
	    	content = response.read().decode('utf-8')
	    	pattern2 = re.compile("<td.*?>.*?<strong.*?>.*?</strong>(.*?)</td>",re.S)#extract news text from every piece of news
	    	items = re.findall(pattern2,content)
	    	for item in items:
	    		f.write(item.encode('gbk'))

f.close()
