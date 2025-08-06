import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('C:/Users/asus/OneDrive/Desktop/chromedriver.exe')

driver = webdriver.Chrome(service=s)

driver.get('https://www.naukri.com/')
time.sleep(5)

user_input = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
time.sleep(3)

user_input.send_keys('AI Engineer')
time.sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[7]/div/div/div[6]').click()
#submit.send_keys(Keys.Enter)
time.sleep(15)

html = driver.page_source
with open('AI_Engineer.html','w', encoding='utf-8') as f:
    f.write(html)
