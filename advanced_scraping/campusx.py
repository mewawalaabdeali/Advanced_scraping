from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


s = Service("C:/Users/asus/OneDrive/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=s)


driver.get('http://google.com')
time.sleep(2)

#fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
user_input.send_keys('CampusX')
time.sleep(2)

user_input.send_keys(Keys.ENTER)

time.sleep(20)