import urllib.request
from cons import headers
import json
import re


def getUrlList():
    req = urllib.request.Request('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')
    req.add_header('user-agent', headers())
    html = urllib.request.urlopen(req, data=b'q&viewFlag=A&sortType=default&searchStyle=&searchRegion=city%3A&searchFansNum=&currentPage=1&pageSize=100').read().decode('gbk')
    # print(html)
    result = json.loads(html)
    return result['data']['searchDOList']


def getInfo(userId):
    req = urllib.request.Request('https://mm.taobao.com/self/aiShow.htm?userId=%s' % userId)
    req.add_header('user-agent', headers())
    html = urllib.request.urlopen(req).read().decode('gbk')
    print(html)


def getAlbumUrl(userId):
    req = urllib.request.Request('https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%%20=%s' % userId)
    req.add_header('user-agent', headers())
    html = urllib.request.urlopen(req).read().decode('gbk')
    reg = r'<a class="mm-first" href="//(.*?)" target="_blank">'
    reg1 = r'mm.taobao.com/self/album_photo.htm?(.*?)&album_id=(.*?)&album_flag=0'
    albumList = re.findall(reg, html)[::2]
    albumId = []
    for j in albumList:
        # j.split('album_id')
        albumId.append(j.split('album_id=')[1].split('&')[0])
    return albumId
    # albumId = re.findall(reg1, ''.join(albumList))
    # print(albumId)
    # for n in albumId:
    #     print(n)


def getPicture(userId, album_id):
    req = urllib.request.Request('https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=%s&album_id=%s' % (userId, album_id))
    req.add_header('user-agent', headers())
    html = urllib.request.urlopen(req).read().decode('gbk')
    result = json.loads(html)
    for k in result['picList']:
        print(k['picUrl'])
    # print(result['picList'])

for i in getUrlList():
    # i['userId']
    # getInfo(i['userId'])
    # getAlbumUrl(i['userId'])
    getPicture(i['userId'], getAlbumUrl(i['userId'])[2])
    break