from tkinter import *
import tkinter as tk
import tkinter.messagebox
# from urllib.error import URLError, HTTPError
import urllib.request, re
import urllib.parse
from PIL import Image
import requests


def getImg():
    name = nameEnt.get()
    if not name:
        tkinter.messagebox.showinfo('温馨提示', '你的姓名为空！')
        return
    url = 'http://www.uustv.com/'
    data = {'word': '%s' % name,
            'sizes': 60,
            'fonts': 'jfcs.ttf',
            'fontcolor': '#000000'}
    print(data)
    data = urllib.parse.urlencode(data).encode(encoding='UTF8')  # python3 需要加的东东
    html = urllib.request.urlopen(url, data=data)
    html = html.read().decode('utf-8')  # 此处进行转字符串，后面正则餐朱为str
    print(html)
    reg = r'<div class="tu">﻿<img src="(.*?)"/>'
    print(type(re.findall(reg, html)[0]))
    imgurl = 'http://www.uustv.com/%s' % re.findall(reg, html)[0]
    urllib.request.urlretrieve(imgurl, '%s.gif' % name)
    try:
        im = Image.open('%s.gif' % name)
        im.show()
        im.close()
    except Exception as e:
        print('请自行打开图片')


root = tk.Tk()
root.geometry('480x100+700+400')
root.title('个性签名设计')
label = tk.Label(root, text='姓名:', font=("微软雅黑", 20), fg='red')
label.grid()  # 布局
nameEnt = tk.Entry(root, font=("微软雅黑", 20))
nameEnt.grid(row=0, column=1)
button = tk.Button(root, text='生成签名', font=("微软雅黑", 15), width='15', command=getImg)
button.grid(row=1, column=1)
mainloop()


