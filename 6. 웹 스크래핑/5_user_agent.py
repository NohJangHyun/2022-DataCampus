#특정 웹사이트의 경우 접속할 때 받는 header 정보에 따라 제공하는 페이지가 달라짐
#but 사람 대신 컴퓨터가 접속해 무단으로 정보를 가져가려는 경우 사이트에서 접속을 차단할 수 있음
import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status()

with open('nadocoding.html', 'w', encoding='utf-8') as f:
    f.write(res.text)  