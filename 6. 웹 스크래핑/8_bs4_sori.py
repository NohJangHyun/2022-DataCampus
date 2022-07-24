#완결된 마음의 소리 제목 + 링크 가져오기
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=20853"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title, "https://comic.naver.com" + link) #맥은 cmd + 링크 클릭하면 브라우저에서 확인 가능

#제목 + 링크 여러 개 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)


#평점 정보 가져와서 평균 계산하기
total_rate = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rate += float(rate)

print("전체 점수 : ", total_rate)
print("평균 점수 : ", total_rate/len(cartoons))
