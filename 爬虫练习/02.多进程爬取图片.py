import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import os


def getHtml(url):
    try:
        r = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('无法获取页面数据')


def getUrl(html, url_list):
    soup = BeautifulSoup(html, 'html.parser')
    for themes in soup.find_all('section', attrs={'class': 'photos'})[1].contents[1].find_all('a'):
        url = 'http://wallls.com' + themes.get('href')
        url_list.append(url)


def get_pic_url(urls):
    pic_list = []
    themes = urls.split('/')[-2]
    try:
        r = requests.get(urls, headers={'user-agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = 'utf-8'
        html = r.text
    except:
        print('无法获取页面数据2')
    soup = BeautifulSoup(html, 'html.parser')
    for pic_urls in soup.find('div', attrs={'class': 'images'}).find_all('img'):
        pic_urls = pic_urls.get('src')
        pic_list.append(pic_urls)
    print('dowloading...... 图集　%s 正在下载中！！！' % (themes))
    dowload_pic(pic_list, themes)


def dowload_pic(pic_list, themes):
    for pic_url in pic_list:
        try:
            pic_data = requests.get(pic_url, headers={'user-agent': 'Mozilla/5.0'})
            pic_data.raise_for_status()
            pic_data.encoding = 'utf-8'
            pic = pic_data.content
        except:
            print("")
        if not os.path.exists(themes):
            os.mkdir(themes)
        with open('{}/{}'.format(themes, pic_url.split('/')[-1]), 'wb') as f:
            f.write(pic)

#进程池
def dowload_all_pic(url_list):
    with Pool(2) as p:
        p.map(get_pic_url, url_list)


def main():
    url = "http://wallls.com/"
    html = getHtml(url)
    url_list = []
    getUrl(html, url_list)
    dowload_all_pic(url_list)

main()

