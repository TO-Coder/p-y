import csv
import requests
import pandas as pd

url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"
headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
}
respones = requests.get(url, headers=headers)
data = respones.json()
data1 = []

for i in data:
    name = i['title']
    rating = i['rating']
    number = i['id']
    pictures = i['cover_url']
    print(name, rating, number, pictures)

    data1.append([name, rating, number, pictures])
df = pd.DataFrame.from_records(data1,columns=['电影名称','电影评分','评价人数','电影图片'])
df.to_csv('douban_movies.csv', index=False)
print("数据已保存到 douban_movies.csv")