import urllib.request, re


def page(pg):
    url = 'https://www.pengfu.com/index_%s.html' % pg
    html = urllib.request.urlopen(url).read().decode('utf-8')
    #print(html)
    return html


def title(html):

    reg = re.compile(r'<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a>')  #()里面的东西需要取出来
    item = re.findall(reg, html)
    # print(item)
    # for t in item:
    #    print(t)
    return item


def content(html):
    reg = r'<img src="(.*?)" width='
    item = re.findall(reg, html)
    return item


def download(url, name):
    path = 'img\%s.gif' % name
    urllib.request.urlretrieve(url, path)


for i in range(1, 3):
    html = page(i)
    title_list = title(html)
    content_list = content(html)
    for y, z in zip(title_list, content_list):
        # download(z, i)
        print(z, y)

















#from bs4 import BeautifulSoup


#html = 'https://www.pengfu.com'
#soup = BeautifulSoup(open('a.html'))
#print(soup.prettify())







#html = "<div>菜鸟的世界</div>"
#Esoup = BeautifulSoup(html, 'html.parser')  # 解析网页，（网址，解析方式）
#print(soup.div)
