import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

movie_info = soup.select('div.tit5')
for movie in movie_info:
    print("*" * 60)
    title_el = movie.select('a')
    point_el = movie.select('td.point')
    if len(title_el) > 0:
        title = title_el[0].text
        print(title)
    if len(point_el) > 0:
        point = point_el[0].text
        print(point)
