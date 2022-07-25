#selenium - 웹 페이지 테스트 자동화 프레임워크
#Pip install selenium 진행, 크롬 버전에 맞는 webdriver 다운로드 후 같은 파일에 압축 풀기
from selenium import webdriver
from selenium.webdriver.common.by import By

# browser = webdriver.Chrome("./chromedriver") #webdriver 객체 생성 후
# browser.get("http://naver.com") #그 브라우저에서 주어진 url로 이동
# browser.implicitly_wait(10)
# elem = browser.find_element(By.CLASS_NAME, "link_login")


# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# for e in elem:
#     e.get_attribute("href")



browser = webdriver.Chrome("./chromedriver") #webdriver 객체 생성


import time
#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인 이동
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

#3. id, pw 이동
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("password")

#4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()
time.sleep(3)

#5. id를 새로 입력
# browser.find_element(By.ID, "id").send_keys("my_id")
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

#6. html 정보 출력
print(browser.page_source)

#7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() #전체 브라우저 종료