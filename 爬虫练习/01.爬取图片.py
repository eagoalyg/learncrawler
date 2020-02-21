import requests
import os
from bs4 import BeautifulSoup
import datetime


def getHTMLText(url, headers):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('爬取失败')


def parseHTML(html, pic_urls):
    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.find('div', attrs={'id':'main'}).find_all('a'):
        pic_url = i.find('img').get('src')
        pic_urls.append(pic_url)


def save_pic(pic_urls, name, headers):
    for pic_url in pic_urls:
        content = requests.get(pic_url, headers=headers).content
        with open('{}/{}'.format(name, pic_url.split('/')[-1]), 'wb') as f:
            f.write(content)


def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)


def main():
    print(datetime.datetime.now())
    url = 'https://stocksnap.io/view-photos/sort/trending/desc'
    name = 'stocksnap'
    path = create_dir(name)
    headers = {'user-agent':'Mozilla/5.0'}
    pic_urls = []
    html = getHTMLText(url, headers)
    parseHTML(html, pic_urls)
    save_pic(pic_urls, name, headers)
    print(datetime.datetime.now())
    

main()
