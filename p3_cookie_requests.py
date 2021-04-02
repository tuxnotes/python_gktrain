import requests
import time
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'user-agent': ua.random
}

s = requests.Session()
# 回话对象：在同一个Session实例发出的所有请求之间保持cookie，期间使用
login_url = 'https://account.douban.com/j/mobile/login/basic'
form_data = {
    'ck': '',
    'name': '15055495@qq.com',
    'password': 'test123test123',
    'remember': 'false',
    'ticket': ''
}

# 下面请求成功后s就有cookie的信息了
response = s.post(login_url,data=form_data, headers=headers)

url2 = 'https://www.douban.com/accounts'
response2 = s.get(url2,headers=headers) # 这里会自动携带cookie信息

with open('profile.html', 'w+') as f:
    f.write(response2.text)

