import requests
import json
from bs4 import BeautifulSoup
import re

city_id = {'北京': '101010100', '上海': '101020100', '广州': '101280101'}
def get_weather():
    url = 'http://www.weather.com.cn/weather1d/101010100.shtml#search'
    url1 = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
    url2 = 'http://www.weather.com.cn/data/sk/101010100.html'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
    html1 = requests.get(url).content.decode('utf-8')
    html2 = requests.get(url2).content.decode('utf-8')
    # print(html1)
    print(html2)
    # data = json.loads(html)
    # print(data)
    # print(data['weatherinfo']['city'])
    soup = BeautifulSoup(html1, 'html.parser')
    for i in soup.find_all('span'):
        print(i)



get_weather()
