import requests
import json

query=input("what type of new are you interested in? ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-12-04&sortBy=publishedAt&apiKey=d8e656c868c14006a65f000647c984a3"
r=requests.get(url)
news=json.loads(r.text)
for  i in news["articles"]:
    print(i["title"])
    print(i["description"])
    print(i["content"])
    print(i["publishedAt"])
    print("-------------------------------------------")
