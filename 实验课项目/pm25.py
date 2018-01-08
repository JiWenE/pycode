import requests
import re
import json


def get_url(url):
    # url = 'http://www.pm25.in/api/querys/aqi_ranking.json&token=5j1znBVAsnSf5xQyNQyq'
    request = requests.get(url)
    return request.text
city_list = ['beijing', 'shanghai', 'guangzhou', 'hangzhou', 'tianjin', 'chengdu', 'nanjing', 'xian']

# f = open('citydata.txt', 'w')


def change_data(aim_str):  # 对字符串进行正则表达式提取，将字符串转为字典
    aim = re.compile(r'({.*?})', re.S)
    data = re.findall(aim, aim_str)
    j = 0
    data_list = []
    while j < len(data):
        data_list.append(json.loads(data[j]))
        print(type(data_list[j]))
        j += 1
    return data_list


def get_city_data():  # 获取城市详细数据
    url = 'http://www.pm25.in/api/querys/pm2_5.json?city=%s&token=5j1znBVAsnSf5xQyNQyq'
    for i in range(0, 8):
        start_url = url % city_list[i]
        text = get_url(start_url)
        print(text)
        print('正在获取第%d个城市信息。。。。。' % i)
        # data_list = change_data(text)
        # for k in data_list:
        #     f.write(str(k)+'\n')
        # f.write('\n'*2)
        f = open('citydata/%s.json' % city_list[i], 'w')
        f.write(text)
        f.close()
        print('保存完毕')


def get_whole_data():  # 获取所有城市质量信息
    url = 'http://www.pm25.in/api/querys/aqi_ranking.json&token=5j1znBVAsnSf5xQyNQyq'
    text = get_url(url)
    f = open('whole_data.json', 'w')
    f.write(text)
    f.close()

get_city_data()
get_whole_data()




