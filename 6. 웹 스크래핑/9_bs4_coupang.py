#bs4 활용 2-1(쿠팡) - 코드 안돌아감


#GET: 누구나 볼 수 있게 URL로 보냄
#POST: URL이 아닌 HTTP body 안에 숨겨서 보냄(ID,PW)
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"}
res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()
    price = items.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})

    if rate_cnt:
        rate = rate_cnt.get_text()
    else:
        rate = "평점 수 없음"
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})

    print(name, price, rate, rate_cnt)