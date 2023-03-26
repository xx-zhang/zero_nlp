# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import collections
import re
import os
import time
import sys
import types

"""
Reffer: https://github.com/Jack-Cherish/python-spider/blob/master/biqukan.py
类说明:下载《笔趣看》网小说: url:https://www.biqukan.com/
Parameters:
	target - 《笔趣看》网指定的小说目录地址(string)
Returns:
	无
Modify:
	2017-05-06
"""

BIQUKAN_SITE_HOST = "https://www.biqukan8.cc/"
COMMON_HEADERS = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',}

def fetch_request(target_url):
    target_req = request.Request(url=target_url, headers=COMMON_HEADERS)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk', 'ignore')
    return BeautifulSoup(target_html, 'lxml')
    


def get_novel_list():
    url = "http://m.biqu520.net/sort-1-220/"


    pass 


def get_download_url(target_url):
    # charter = re.compile(u'[第弟](.+)章', re.IGNORECASE)
    listmain_soup = fetch_request(target_url)
    chapters = listmain_soup.find_all('div',class_ = 'listmain')

    download_soup = BeautifulSoup(str(chapters), 'lxml')
    # novel_name = str(download_soup.dl.dt).split("》")[0][5:]
    novel_name = re.findall("《(.*?)》", str(download_soup.dl.dt))[0]
    flag_name = "《" + novel_name + "》" + "正文卷"
    numbers = (len(download_soup.dl.contents) - 1) / 2 - 8

    info = listmain_soup.find_all('div', class_ = 'small')
    summary = listmain_soup.find_all('div', class_ = 'intro')

    download_dict = collections.OrderedDict()
    begin_flag = False
    numbers = 1
    for child in download_soup.dl.children:
        if child != '\n':
            if child.string == u"%s" % flag_name:
                begin_flag = True
            if begin_flag == True and child.a != None:
                download_url = BIQUKAN_SITE_HOST + child.a.get('href')
                download_name = child.string
                # print(download_name)
                try:
                    name = re.findall("[第弟](.*)[张章]", download_name)[0]
                    dict_key = f'第{str(numbers)}章-{name}'
                except Exception as e:
                    dict_key = download_name
                if name:
                    download_dict[dict_key] = {"download_url": download_url, "numbers": numbers}
                    numbers += 1

    return novel_name, info, summary, download_dict


def downloader(url):
    download_req = request.Request(url = url, headers = COMMON_HEADERS)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('gbk','ignore')
    soup_texts = BeautifulSoup(download_html, 'lxml')
    texts = soup_texts.find_all(id = 'content', class_ = 'showtxt')
    soup_text = BeautifulSoup(str(texts), 'lxml').div.text.replace('\xa0','')
    return soup_text
    

def download_txt_url(target_url):
    novel_name, info, summary, download_dict = get_download_url(target_url)
    print(download_dict)


if __name__ == "__main__":
    # print("\n\t\t欢迎使用《笔趣看》小说下载小工具\n\n\t\t作者:Jack-Cui\t时间:2017-05-06\n")
    print("*************************************************************************")
    
    #小说地址
    # target_url = str(input("请输入小说目录下载地址:\n"))
    target_url = "https://m.biqukan8.cc/24344_24344372/"

    download_txt_url(target_url) 
