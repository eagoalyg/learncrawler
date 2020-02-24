import requests
from bs4 import BeautifulSoup
import csv
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def saveValues(ulist):
    with open('univList.csv', 'w') as f:
        fieldnames = ['排名', '学校名称', '分数']

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(len(ulist)):
            u = ulist[i]
            writer.writerow({fieldnames[0]: u[0], fieldnames[1]: u[1], fieldnames[2]: u[2]})


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    saveValues(uinfo)


main()
