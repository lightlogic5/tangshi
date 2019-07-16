import json
import os
from urllib.parse import urlencode
import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import re
from multiprocessing import Pool
from hashlib import md5
from json.decoder import JSONDecodeError




def get_page_index():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    url = 'https://so.gushiwen.org/gushi/tangshi.aspx'
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None

def parse_page_index(html):
    pattern = re.compile('<span><a href="(.*?)".*?>(.*?)</a>', re.S)
    items = re.findall(pattern, html)
    url1 = 'https://so.gushiwen.org'
    for item in items:
        yield {
            'title': item[1],
            'url': url1 + item[0]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def get_shi(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            shi = response.text
            pattern = re.compile('<div class="contson".*?>(.*?)</div>', re.S)
            tangshi = re.search(pattern,shi).group(1).strip().replace('<br />|(.*?\\)','')

            return tangshi
        return None
    except ConnectionError:
        print('Error occurred')
        return None

def main():
    html = get_page_index()
    i = 1
    for url in parse_page_index(html):
        i = i+1
        ts = get_shi(url['url'])
        write_to_file(ts)
    print(i)


if __name__ == '__main__':
    main()




   