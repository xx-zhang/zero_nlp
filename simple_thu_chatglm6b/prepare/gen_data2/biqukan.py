# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import collections
import re
import os 
import time 
import concurrent.futures


BIQUKAN_SITE_HOST = "https://www.biqukan8.cc/"
COMMON_HEADERS = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',}

def fetch_request(target_url):
  target_req = request.Request(url=target_url, headers=COMMON_HEADERS)
  target_response = request.urlopen(target_req)
  target_html = target_response.read().decode('gbk', 'ignore')
  return BeautifulSoup(target_html, 'lxml')


def get_novel_pager_list(cate_id=1, pager=2):
    url = f"http://m.biqu520.net/sort-{cate_id}-{pager}/"
    temp_soup = fetch_request(url)
    novel_list_soup = temp_soup.find_all('p', class_ = 'line')
    temp_res = []
    if novel_list_soup:
        for x in novel_list_soup:
            partern = '<p class="line"><a href=".*?">\[(.*?)\]</a><a.*?href="/info-(\d+)/".*?>(.*?)</a>/<a href="/author/(.*?)">.*?</a></p>'
            match_data = re.match(partern, str(x))
            if match_data:
                temp_data = dict(
                    novel_category = match_data.group(1), 
                    # novel_url = match_data.group(2),
                    novel_id = match_data.group(2),
                    novel_name = match_data.group(3), 
                    novel_author = match_data.group(4), 
                )
                temp_res.append(temp_data)
    return temp_res


def fetch_chapter_from_url(pager=1, novel_id=33044, get_max_pager=False):
    num_per_page = 20
    url = f"http://m.biqu520.net/wapbook-{novel_id}_{pager}/"
    temp_soup = fetch_request(url)
    # print(temp_soup)
    __pager_soup = temp_soup.find_all('div', class_ = 'page')
    pager_matcher = re.match(".*\(第(\d+)/(\d+)页\)当前20条/页.*", str(__pager_soup))
    max_pager = int(pager_matcher.group(2))
    if get_max_pager:
        return max_pager
    cur_pager = int(pager_matcher.group(1))
    # if cur_pager != max_pager:
    #     have_next = True 
    chapter_soup = temp_soup.find_all('ul', class_ = 'chapter')[0]
    chapter_list = [] 

    partern = '<li><a href="(/wapbook-\d+-\d+/)">(.*?)<span></span></a></li>'
    matched_data = re.findall(partern, str(chapter_soup))
    index = 1 
    for x in matched_data:
        cur_chaper_number = cur_pager* num_per_page + index 
        temp_data = dict(
            chapter_name=x[1], 
            chapter_url=x[0],
            chapter_num=cur_chaper_number)
        index += 1
        chapter_list.append(temp_data)
    return chapter_list


def get_chapter_content(chapter_url):
    time.sleep(1)
    url = f"http://m.biqu520.net{chapter_url}"
    # print(url)
    temp_soup = fetch_request(url)
    text_soup = temp_soup.find_all('div', class_ = 'text')
    return str(text_soup)

NOVAL_SAVE_DIR = "/novel_data"

def download_novel_chapter_task(chapter_info):
    chapter_url = chapter_info["chapter_url"]
    chapter_name = chapter_info["chapter_name"]
    novel_category = chapter_info["novel_category"]
    # chapter_id = re.match(".*?/(\d+)/$", chapter_url).group(1)
    chapter_num = chapter_info["chapter_num"]
    novel_content = get_chapter_content(chapter_url)
    novel_save_path = os.path.join(
        NOVAL_SAVE_DIR, 
        novel_category,
        f"{chapter_info['novel_id']}-{chapter_info['novel_name']}", 
        f"{chapter_num}-{chapter_name}")
    novel_save_dir = os.path.dirname(novel_save_path)
    if not os.path.exists(novel_save_dir):
        os.makedirs(novel_save_dir)
        
    with open(novel_save_path, "w", encoding="utf-8") as f:
        f.write(novel_content)
        f.close()
        
    return novel_save_path

def main(cate_id=1, max_category_pager=200):
    # count = 1 
    for pager in [i+1 for i in range(max_category_pager)]:
        # TODO 获取 novel 列表
        novel_list = get_novel_pager_list(cate_id=cate_id, pager=pager)
        for novel in novel_list:
            novel_category = novel["novel_category"]
            novel_id = novel["novel_id"]
            novel_name = novel["novel_name"]
            # novel_author = novel["novel_author"]
            max_chapter_page = fetch_chapter_from_url(novel_id=novel_id, get_max_pager=True)
            # 获取章节的列表，开始将20个章节一起下载。
            for pager in [i+1 for i in range(max_chapter_page)]:
                chapter_list = fetch_chapter_from_url(pager=pager, novel_id=novel_id)
                all_chapter_info = [dict(
                    **x, 
                    novel_category=novel_category, 
                    novel_id=novel_id, 
                    novel_name=novel_name) for x in chapter_list]
                with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
                    tasks = [executor.submit(download_novel_chapter_task, chapter_info) for chapter_info in all_chapter_info]
                    for future in concurrent.futures.as_completed(tasks):
                        result = future.result()
                        print(f"Task returned {result}")


def test():
    print("*************************************************************************")
    chapter_list = fetch_chapter_from_url(pager=1, novel_id=33044, get_max_pager=False)
    for x in chapter_list:
        # print(x)
        chapter_url = x["chapter_url"]
        chapter_content = get_chapter_content(chapter_url=chapter_url)
        print(chapter_content)
        break 


if __name__ == "__main__":
    # print("\n\t\t欢迎使用《笔趣看》小说下载小工具\n\n\t\t作者:Jack-Cui\t时间:2017-05-06\n")

    main(cate_id=1, max_category_pager=10)
