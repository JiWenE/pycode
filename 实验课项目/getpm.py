import urllib.request
from bs4 import BeautifulSoup
import re


def get_url(city):
    city_dict = {'北京': 'beijing', '上海': 'shanghai', '广州': 'guangzhou'}
    url = 'http://www.pm25.in/%s' % city_dict[city]
    html = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # reg = r'<div class="affect">(.*?)</div>'
    # a = re.findall(reg, html)[0]
    # print(a)
    for j in soup.find_all('div', class_='span1'):
        # print(j.find_all('div'))
        try:
            print(j.find_all('div')[1].string.strip()+':'+j.find_all('div')[0].string.strip())
        except IndexError:
            pass
    for i in soup.find_all('p'):
        if i.string == None:
            pass
        else:
            print(i.string.replace('\n', '').replace(' ', ''))


get_url('北京')
