import requests
from bs4 import BeautifulSoup
import bs4  


def getHTMLText(url):
    try:
        r = requests.get(url, headers={'user-agent':'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("error")


def parsePage(ilt, html):
    soup = BeautifulSoup(html, 'html.parser')
    for goods in soup.find_all('div', attrs={"class":"gl-i-wrap"}):
        name = goods.find(attrs={"class":"p-name p-name-type-2"}).a.em.text
        price = goods.find(attrs={"class":"p-price"}).strong.i.string
        ilt.append([name, price])


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品"))
    count = 0
    for goods in ilt:
        count += 1
        print(tplt.format(count, goods[1], goods[0]))


def main():
    goods = input("爬取商品名称:")
    while True:
        try:
            depth = int(input("爬取页数:"))
            break
        except:
            print("输入错误!!!")
    start_url = 'https://search.jd.com/Search?keyword=' + goods + '&enc=utf-8'
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&page=' + str((i+1)*2-1)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()
