import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(URL)
web=response.text

soup=BeautifulSoup(web,"html.parser")

names=soup.select(".article-title-description__text .title")
titles=[title.getText() for title in names]
titles=titles[::-1]

with open('movies.txt','w') as f:
    for line in titles:
        f.write(f"{line}\n")




