import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
url = 'https://www.naver.com/'
driver.get(url)

driver.find_element(By.XPATH,'//*[@id="account"]/div/a').click()
