#-*- coding:utf8 -*-


import requests
headers = {
'User-Agent': 'Mozilla/5.0'
}
r = requests.get("https://news-at.zhihu.com/api/4/news/latest",headers = headers)
print(r.status_code)
print(r.json())