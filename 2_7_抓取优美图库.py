# 1. 拿到主页面的源代码，然后提取到子页面的链接地址，href
# 2. 通过href拿到子页面的内容，从子页面中找到图片的下载地址 img -> src
# 3. 下载图片
import re

import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umeituku.com/bizhitupian/diannaobizhi/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://www.umei.cc/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

resp = requests.get(url, headers)
resp.encoding = "utf-8"  # 处理乱码

# 把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a")
for a in alist:
    href = a.get('href')  # 直接通过get就可以拿到属性的值
    # 拿到子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    div = child_page.find("div", class_='ImageBody').find("img")
    src = div.get('src')
    # 下载图片
    img_resp = requests.get(src)
    # img_resp.content # 这里拿到的是字节
    img_name = src.split("/")[-1] # 拿到url中最后一个/以后的内容
    with  open(img_name, mode="wb") as f:
        f.write(img_resp.content) # 图片内容写入文件

    print("over", img_name)
    time.sleep(1)
print("all over")


