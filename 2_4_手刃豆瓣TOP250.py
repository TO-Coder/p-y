# 拿到页面源代码     requests
# 通过re来提取想要的有效信息  re
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p>.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<pj>.*?)</span>', re.S)
# 开始匹配
result = obj.finditer(page_content)
f = open("data.csv", mode="w")
csvwriter = csv.writer(f)
for i in result:
    # print(i.group("name"))
    # print(i.group("score"))
    # print(i.group("pj"))
    # print(i.group("year").strip())
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())

f.close()
resp.close() # 关闭resp



