import requests

r = requests.get('https://api.github.com/events')
r.headers['Content-Type']
r.text
r.encoding
r.json()

# 传递URL
payload={'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
r.url

# 定制头部
# 全链路跟踪，在header中加入很多标记。在比如微博，其api的header中也是有很多定制的header
header = {'user-agent': 'safari'}
r = requests.get('http://httpbin.org/get',headers=header)
