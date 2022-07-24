#pip install beautifulsoup4 - 스크래핑하기 위한 패키지 
#pip install lxml - 구문 분석을 위한 parser
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

#가져온 html 문서를 lxml parser를 통해 beautifulsoup를 만들고 soup가 모든 정보 가지고 있음
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #soup에서 첫 번째로 발견 되는 a 태그 정보 출력
# print(soup.a.attrs) #a 태그가 가지고 있는 속성 확인할 수 있음
# print(soup.a["href"]) #a 태그의 href 값(속성)만 가져오고 싶은 경우

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) #클래스가 Nbtn_upload인 a element 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) #클래스가 Nbtn_upload인 element 찾아줘


#인기 급상승 웹툰 top1 정보 가져오기
#li 태그, class명 rank01
# print(soup.find("li", attrs={"class":"rank01"}))

#인기 급상승 웹툰 top1 링크만 가져오기
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)

#인기 급상승 웹툰 top1~3 문자 가져오기(next_sibling)
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text()) #글자 가져오괴
# print(rank1.next_sibling) 
# rank2 = rank1.next_sibling.next_sibling # 태그 사이에 줄 바꿈이 있기 떄문에 next_sibling 두번 사용
# rank3 = rank2.next_sibling.next_sibling
# print(rank1.a.get_text())
# print(rank2.a.get_text())
# print(rank3.a.get_text())

#인기 급상승 웹툰 top2 문자 가져오기(previous_sibling)
# rank3 = soup.find("li", attrs={"class":"rank03"})
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

#인기 급상승 웹툰의 parent 불러오기(parent)
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.parent)



#next_sibling, previous_sibling 두번 사용하기 귀찮을 때
# rank1 = soup.find("li", attrs={"class":"rank01"})
# rank2 = rank1.find_next_sibling("li") #조건에 해당하는 것만
# print(rank2.a.get_text())
# rank1 = rank2.find_previous_sibling()
# print(rank1.a.get_text())


#한번에 모든 정보 불러오기(find_next_siblings)
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.find_next_siblings("li"))


#text로도 find 가능
# webtoon = soup.find("a", text="99강화나무몽둥이-18화. ONE LOVE (2)") 
# print(webtoon)
