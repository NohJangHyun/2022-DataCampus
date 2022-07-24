import requests #웹 페이지의 문서 정보를 가져오기 위한 라이브러리

res = requests.get('http://google.com') #원하는 url 정보 넘겨주고, 가져온 정보를 res에 담는다
res.raise_for_status() #문제 발생시 오류 출력 후 break / print(res.status_code) 방법 사용시 문제 없으면 200 출력됨

print(len(res.text)) #원하는 url의 html 문자열의 길이 확인
print(res.text) #원하는 url의 html 문자열 확인

with open('mygoogle.html', 'w', encoding='utf-8') as f:
    f.write(res.text) #위의 text를 mygoogle.html 파일로 생성




