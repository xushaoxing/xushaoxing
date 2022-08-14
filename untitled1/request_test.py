import json

import requests
from PIL import Image
# r=requests.get('http://httpbin.org/ip')
# r = requests.post('http://httpbin.org/post', data={'name': 'leo'})

# d = {'key1': '1', 'key2': '2'}
# r = requests.get('http://httpbin.org/get', params=d)
# # print(r)
# print(r.status_code)
# # print(r.url)
# print(r.text)
# print(r.headers)
# # print(r.json())

# 可以将一json串传给requests.post()的data参数，
url = 'http://httpbin.org/post'
s = json.dumps({'key1': '1', 'key2': '2'})
r = requests.post(url, data=s)
print (r.text)


# # 如果状态码是40X或者50X，那么可以使用Response.raise_for_status()抛出一下异常：
# r = requests.get('http://httpbin.org/status/404')
# print (r.raise_for_status())

# r = requests.get('http://httpbin.org/ip')
# d = r.json()
# print (d)
# print (d['origin'])

