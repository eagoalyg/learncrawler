import requests


url = "http://www.baidu.com"

try:
    r = requests.get(url)
    r.raise_for_status()    #如果没有返回200则返回异常
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")
