# 小文件下载

import requests

image_url = "https://www.python.org/static/community_logos/python_logo"
r = requests.get(image_url)

with open('python_logo.png', 'wb') as f:
    f.write(r.content)


# 大文件下载
# 如果文件比较大，下载下来的文件先放内存，则内存的压力很是很大的，此时请求的时候采用流的形式

file_url = 'http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2'
r = requests.get(file_url, stream=True)
with open('python.pdf', 'wb') as pdf:
    for chunk in r.iter_content(1024):
        if chunk:
            pdf.write(chunk)