import requests,threading
from lxml import etree
from bs4 import BeautifulSoup


def get_html(url):
    # url = 'https://www.doutula.com/article/list/?page={}'.format(a)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    request = requests.get(url=url, headers=headers)
    response = request.content
    return response


# 匹配图片
def get_img_html(html):
    soup = BeautifulSoup(html, 'xml')
    all_a = soup.find_all('a', class_='list-group-item')
    print(all_a)
    for i in all_a:
        img_html = get_html(i['href'])  # 获取源码
        return img_html


# 获取图片url
def get_img(html):
    soup = etree.HTML(html)  # 初始化源码
    items = soup.xpath('//div[@class="artile_des"]')
    for item in items:
        imgurl_list = item.xpath('table/tbody/tr/td/a/img/@onerror')
        return imgurl_list
# 下载图片
x = 1


def save_img(img_url):
    global x
    x += 1
    img_url = img_url.split('=')[-1][1:-2].replace('jp', 'jpg')
    print("正在下载"+'http:'+img_url)
    img_content = requests.get('http:' + img_url).content
    with open('斗图/%s.jpg' % x) as f:
        f.write(img_content)


def start_save_img(imgurl_list):
    for i in imgurl_list:
        print(i)
        th = threading.Thread(target=save_img, args=(i,))
        th.start()


# 主函数
def main():
    start_url = 'https://www.doutula.com/article/list/?page={}'
    for i in range(1, 3):
        start_html = get_html(start_url.format(i))  # 字符串格式化
        img_html = get_img_html(start_html)
        img_list = get_img(img_html)
        start_save_img(img_list)


if __name__ == '__main__':  # 判断文件入口
    main()



