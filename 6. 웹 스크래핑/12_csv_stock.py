#네이버에서 코스피 시가 총액 순위 정보 가져오기

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1-100.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
#["N", "종목명", "현재가"....]
writer.writerow(title)

for page in range(1,2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #공백 데이터 스킵
            continue
        data = [column.get_text().strip() for column in columns]#columns에 있는 것들을 하나씩 가져와서 column이라고 하고, 그 column에서 get_text를 함
        # print(data)
        writer.writerow(data)