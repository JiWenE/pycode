# !/user/bin/env python
# -*- coding:utf-8 -*-
import requests
from html.parser import HTMLParser
from PIL import Image
import getpass
import json

class DoubanClient(object):
    def __init__(self):
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.79 Safari / 537.36',
        #     'referer': 'https://accounts.douban.com/login'
        # }

        self.session = requests.session()  # 会话
        # self.session.headers.update(headers)

    def login(self, username, password, source="index_nav", redir="https://www.douban.com/", login="登录"):
        url = 'https://www.douban.com'
        req = self.session.get(url)
        # print(req.text)
        (captcha_id, captcha_url) = _get_captcha(req.text)
        if captcha_id:
            req = self.session.get(captcha_url)
            with open('captcha.jpg', 'wb') as f:
                f.write(req.content)
                f.close()
            try:
                im = Image.open('captcha.jpg')
                im.show()
                im.close()
            except:
                pass
            # global captcha_solution
            captcha_solution = input('please input the solution:')
        # post_url = 'https://accounts.douban.com/login'
        post_data = {
            'source': source,
            'redir': redir,
            'from_email': username,
            'from_password': password,
            'login': login
            }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.79 Safari / 537.36',
            'referer': 'https://accounts.douban.com/login',
            'Origin': 'https://accounts.douban.com',
            'host': 'accounts.douban.com',
            'Connection': 'keep - alive',
            'Upgrade-Insecure-Requests': '1'

        }
        if captcha_id:
            post_data['captcha-id'] = captcha_id
            post_data['captcha-solution'] = captcha_solution
        print(post_data)
        login = self.session.post(url, data=post_data, headers=headers)
        print(type(login.cookies))
        # get_url = 'https://www.douban.com'
        # print(self.session.get(get_url, headers=headers).text)


def _get_captcha(content):
    '''
    获取验证码id和url
    :param content: 
    :return: 
    '''
    class CaptchParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)  # 初始化
            self.captcha_id = None
            self.captcha_url = None

        def handle_starttag(self, tag, attrs):  # tag=标签 attrs=属性
            if tag == 'img' and _attr(attrs, 'id') == 'captcha_image' and _attr(attrs, 'class') == 'captcha_image':
                self.captcha_url = _attr(attrs, 'src')

            if tag == 'input' and _attr(attrs, 'type') == 'hidden' and _attr(attrs, 'name') == 'captcha-id':
                self.captcha_id = _attr(attrs, 'value')
    p = CaptchParser()
    p.feed(content)  # 把需要哦解析的数据传给feed解析
    return p.captcha_id, p.captcha_url


def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None





if __name__ == '__main__':
    username = input('please input your username:')
    password = input('please input your password:')
    c = DoubanClient()
    c.login(str(username), str(password))
