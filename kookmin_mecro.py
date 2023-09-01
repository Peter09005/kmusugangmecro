import selenium
import threading
import time
import urllib.request
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("no-sandbox")
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

driver = webdriver.Chrome()
url = 'https://sugang.kookmin.ac.kr/slogin'
apply_code = ["1562900-01"]
def sugangApply():
    time.sleep(0.3)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/a[2]").click()
    for code in apply_code:
        driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/form/div/div/div[1]/div/div[3]/div[2]/div/div/input").send_keys(code[0:-3])
        driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/form/div/div/div[2]/button").click()
        while True:
            pass
def findServerTime(m, s):
    global url
    date = urllib.request.urlopen(url).headers['Date']
    time = date[-9:-4]
    min, sec = map(int, time.split(":"))
    if m == min and s == sec:
        return True
    else:
        return False

def sugangClick(sugangBtn):
    while True:
        randTime = random.uniform(0.1,0.13)
        sugangBtn.click()
        window_list = driver.window_handles
        if len(window_list) == 1:
            sugangApply()
            break
        else:
            for idx in window_list:
                if idx != window_list[0]:
                    driver.switch_to.window(idx)
                    driver.close
            driver.switch_to.window(window_list[0])
# 홈페이지 로그인
def sugangLogin():
    global url
    driver.get(url)
    driver.find_element("name","loginId").send_keys('hkt010905')
    driver.find_element("name","loginPwd").send_keys('200518394b!')
    driver.find_element("id","mobileButton").click()
    driver.implicitly_wait(10)
    sugangBtn = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div[1]/a[6]')
    sugangClick(sugangBtn)

min = int(input("분을 입력하세요: "))
sec = int(input("초를 입력하세요: "))

while True:
    if findServerTime(min,sec):
        sugangLogin()
        break



