import requests


url = "http://www.baidu.com"

#获取url的request对象
r = requests.get(url)

#检查请求状态
r.status_code

r.encoding

r.apparent_encoding

#request对象的文本
r.text

#request对象的二进制文件
r.content
