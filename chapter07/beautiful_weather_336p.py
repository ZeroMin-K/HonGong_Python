from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.weather.go.kr/w/weather/now.do")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("city:", location.select_one("city").string)
    print("weather:", location.select_one("wf").string)
    print("min temp:", location.select_one("tmn").string)
    print("max temp:", location.select_one("tmx").string)
    print()
