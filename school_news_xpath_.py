import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'
}


def resp_(url_):
    resp_ = requests.get(url_, headers=headers)

    resp_.encoding = 'utf-8'

    html_ = etree.HTML(resp_.text)

    resp_.close()

    return html_


url = 'https://www.hbsy.cn/xwzx/xyxw.htm'

html = resp_(url)

lis = html.xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/ul/li')

for i in lis:
    title = i.xpath('./a/text()')[0]
    print(title)

    href = i.xpath('./a/@href')[0][2:]
    url = 'https://www.hbsy.cn' + href

    html = resp_(url)
    divs = html.xpath('//*[@id="vsb_content_501"]/div/p')
    for i in divs:
        text = i.xpath('.//text()')
        if (text != []):
            text = text[0]
            print(text)

