# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:00:57 2018

@author: 46799
"""

import re
import requests


def dowmloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
            
        #将图片下载到对应的文件夹，这里要注意文件夹的目录和图片的文件类型
        dir = '../images/' + keyword + '_' + str(i) + '.jpeg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        if i >= 25:
            break


if __name__ == '__main__':
    word = input("Input key word: ")
    url = 'https://image.baidu.com/search/index?tn=baiduimage&word='+word
    result = requests.get(url)
    dowmloadPic(result.text, word)
