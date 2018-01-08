from tkinter import scrolledtext
import tkinter as tk
import tkinter.messagebox
import urllib.request
from bs4 import BeautifulSoup
# from xpinyin import Pinyin

def get_url(city):
    # city_dict = {'北京': 'beijing', '上海': 'shanghai', '广州': 'guangzhou'}
    url = 'http://www.pm25.in/%s' % city
    html = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # reg = r'<div class="affect">(.*?)</div>'
    # a = re.findall(reg, html)[0]
    # print(a)
    for j in soup.find_all('div', class_='span1'):
        # print(j.find_all('div'))
        try:
            text.insert(3.0, j.find_all('div')[1].string.strip() + ':' + j.find_all('div')[0].string.strip() + '\n')
        except TypeError:
            pass
        except IndexError:
            pass
        try:
            print(j.find_all('div')[1].string.strip()+':'+j.find_all('div')[0].string.strip())
        except IndexError:
            pass
    for i in soup.find_all('p'):
        if i.string == None:
            pass
        else:
            try:
                text.insert(9.0, i.string.replace('\n', '').replace(' ', '') + '\n')
            except TypeError:
                pass
            print(i.string.replace('\n', '').replace(' ', ''))


def get_city_name():
    city_name = nameEnt.get()
    text.delete(0.0, 'end')
    if not city_name:
        tkinter.messagebox.showinfo('温馨提示', '你的城市名为空！')
        return
    city_dict = {'北京': 'beijing', '上海': 'shanghai', '广州': 'guangzhou'}
    try:
        name = city_dict[city_name]
    except KeyError:
        tkinter.messagebox.showinfo('温馨提示', '你所输入的城市名不存在！')
        return
    # 以上的异常处理可以用一下代码替换
    # 使用一个数组存放所有城市名称city[]
    # 判断输入城市是否为city[]中城市
    # 将城市名转为汉字
    # 调用get_url()

    text.insert(2.0, city_name + '的空气质量如下：')
    get_url(name)



root = tk.Tk()
root.title('pm2.5查询')
root.geometry('+600+100')

text = scrolledtext.ScrolledText(root, font=("微软雅黑", 10))  # 显示实时信息
text.grid()  # 设置位置

nameEnt = tk.Entry(root, font=("微软雅黑", 20))
nameEnt.grid()

button = tk.Button(root, text="查询", command=get_city_name)
button.grid()

root.mainloop()
