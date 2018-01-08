import urllib.request
import re

def get_url():
    req = urllib.request.Request('http://www.idyjy.com/')
    header = {'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    html = urllib.request.urlopen(req).read().decode('gbk')
    return html

def get_movname():
    req = r'<a class="play-img" target="_blank" href="(.*)" title=(.*?) >'
    movlist = re.findall(req, get_url())
    for i in movlist:
        print(i)
    req1 = r'<a class="play-img" href="(.*)" title=(.*?) target="_blank">'
    movlist1 = re.findall(req1, get_url())
    for n in movlist1:
        print(n)

get_movname()