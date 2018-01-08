import urllib.request
import urllib.parse
import re
import base64


name = '前任3'


def encode_name(mov_name):
    d = mov_name.encode('gbk')
    # print(d)
    base = base64.b16encode(d)
    # print(base)
    string = str(base, 'ascii')
    # print(str)
    str1 = ''
    length = len(string)
    # print(len)
    i = 0
    flag = 0
    while i < length:
        if flag == 0:
            str1 += '%'
            flag = 2
        else:
            str1 += string[i]
            i = i + 1
            flag = flag - 1
    aim_url = 'http://so.idyjy.com/s.asp?w={}'.format(str1)
    return aim_url


def get_url(url):
    req = urllib.request.Request(url)
    header = {'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    html = urllib.request.urlopen(req).read().decode('gbk')
    return html


def get_mov(url):
    # print(get_url(url))
    req = r'<a class="play-img" title="(.*)" href="(.*)" target="_blank">'
    movlist = re.findall(req, get_url(url))
    for i in movlist:
        print(i)
    # req1 = r'<a class="play-img" href="(.*)" title=(.*?) target="_blank">'
    # movlist1 = re.findall(req1, get_url(url))
    # for n in movlist1:
    #     print(n)

name = input("Please input movie name:")
get_mov(encode_name(name))
