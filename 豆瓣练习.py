import requests

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
}

resp = requests.get(url, headers=header)

data = resp.json()

for i in data:
    rank = i['rank']
    title = i['title']
    score = i['score']
    print(rank, title, score)

resp.close()
