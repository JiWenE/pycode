# !/user/bin/env python
# -*- coding:utf-8 -*-

from urllib import request
import re

first_url = 'http://www.quanshuwang.com/book/9/9055/'

html = request.urlopen(first_url).read().decode('gbk')

novel_info = {}
novel_info['title'] = re.findall(r'<div class="chapName">.*?<strong>(.*?)</strong>', html)
novel_info['author'] = re.findall(r'<div class="chapName"><span class="r">(.*?)</span>', html)
list1 = re.findall(r'<li><a href="(.*?)" title=".*?">.*?</a></li>', html)
list2 = re.findall(r'<li><a href=".*?" title="(.*?)">.*?</a></li>', html)
print(novel_info)
for i in range(0, len(list1)):
    list1[i] = '%s%s' % (first_url, list1[i])
    print(list2[i] + ':' + list1[i])

# print(html)