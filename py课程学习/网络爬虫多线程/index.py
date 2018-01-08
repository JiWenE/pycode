# 斗图网抓图
import requests,threading
from lxml import etree
from bs4 import BeautifulSoup


# url = 'https://www.doutula.com/article/list/?page=1'
def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    request = requests.get(url=url, headers=headers)
    response = request.content
    return response


def get_img_html(html):
    soup = BeautifulSoup(html, 'xml')
    all_a = soup.find_all('a', class_='list-group-item')
    # print(all_a)
    for i in all_a:
        img_html = get_html(i['href'])
        soup = etree.HTML(img_html)
        items = soup.xpath('//div[@class="artile_des"]')
        for item in items:
            imgurl_list = item.xpath('table/tbody/tr/td/a/img/@onerror')
            start_save_img(imgurl_list)

x = 1
def save_img(img_url):
    global x
    img_url = img_url.split('=')[-1][1:-2].replace('jp', 'jpg')
    print("正在下载"+'http:'+img_url)
    img_content = requests.get('http:' + img_url).content
    with open('doutu/%s.jpg' % x, 'wb') as f:
        f.write(img_content)
        x += 1


def start_save_img(imgurl_list):
    for i in imgurl_list:
        print(i)
        th = threading.Thread(target=save_img, args=(i,))
        th.start()


start_url = 'https://www.doutula.com/article/list/?page=%d'
for i in range(1, 3):
    url = start_url % i
    get_img_html(get_html(url))

