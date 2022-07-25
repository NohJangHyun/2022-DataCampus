from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/"
browser.get(url)
time.sleep(3)
browser.find_element(By.LINK_TEXT, "가는 날").click()
time.sleep(3)

#이번 달 27, 28일 선택
browser.find_element(By.LINK_TEXT, "27")[0].click()
browser.find_element(By.LINK_TEXT, "28")[0].click()
