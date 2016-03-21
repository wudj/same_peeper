#!/usr/bin/python
# -*- coding:utf-8 -*-  
import re
import urllib
import random
import os
import os.path

def getHtml(url):
	page = urllib.urlopen(url)
	return page.read()

def getImg(html,x):
    reg = r'"photo":"(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
	print imgurl
        try:
            urllib.urlretrieve(imgurl.replace('\\',''),'image/%s.jpg' % x)
            x+=1 
        except Exception as e:
            print 'error,continue.',e
    print 'done'

    regNext = r'"next":".*?senses(.+?)"'
    imgNext = re.compile(regNext)
    match = re.search(imgNext,html);
    if match:
        return (match.group(1),x)

url = "http://v2.same.com/channel/1033563/senses"
urltemp = url
x=0
while 1:
    print urltemp
    (img,x) = getImg(getHtml(urltemp),x)
    if img:
        urltemp = url + img
    else:
        print 'over'
        break

