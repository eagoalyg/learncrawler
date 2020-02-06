import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30, headers={'user-agent':'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "" 


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.search(r"([s][hz])(\d{6})", href).group(2))
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-info'})
            name = stockInfo.find('div', attrs={'class':'stock-name'}).h1
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')

        except:
            traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'https://www.laohu8.com/stock/'
    output_file = '/home/eagoalyg/桌面/LaohuStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()
