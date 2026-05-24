from DrissionPage import ChromiumPage
import datetime
import csv

f = open('抖音评论.xlsx', 'w', encoding='utf-8-sig', newline='')
c = csv.DictWriter(f, fieldnames=['昵称', '时间', '地点', '评论'])
c.writeheader()  # 写入表头

web = ChromiumPage()

web.get('https://www.douyin.com/video/7441030870259010870')

# 取决于你要获取多少页数据
for i in range(3):
    # 1. 开启数据包监听
    web.listen.start('aweme/v1/web/comment/list/')

    # 2. 等待数据包监听
    resp = web.listen.wait()

    # 3. 拿到数据包中的内容
    json_data = resp.response.body

    # 4. 解析数据
    for i in json_data['comments']:
        comment = i['text']
        name = i['user']['nickname']
        time = i['create_time']
        time = datetime.datetime.fromtimestamp(time)
        addr = i['ip_label']

        dict1 = {
            '昵称': name,
            '时间': time,
            '地点': addr,
            '评论': comment,
        }
        c.writerow(dict1)
