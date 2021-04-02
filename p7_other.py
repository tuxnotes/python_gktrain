import requests

# SSL证书
# 如果将verify设置为true,requests也能会略对SSL证书的验证
requests.get('https://kennethreitz.org', varify=False)
# <Response 200>

# 客户端证书
# 你也可以指定一个本地证书作为客户端证书，可以是单个文件(包含证书和秘钥)或者一个
requests.get('https://kennethreitz.org', cert=('/path/client.cert',))
# <Response 200>