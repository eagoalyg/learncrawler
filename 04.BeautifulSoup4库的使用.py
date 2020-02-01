import requests
from bs4 import BeautifulSoup   #必须先安装BeautifulSoup4库


url = "http://www.baidu.com"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    print(soup.prettify())
except:
    print("错误")
