from selenium import webdriver
import time
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

#s = Service("C:/Users/asus/OneDrive/Desktop/chromedriver.exe")
f = Service("C:/Projects/geckodriver-v0.36.0-win-aarch64/geckodriver.exe")

#driver = webdriver.Chrome(service=s)
firedrive = webdriver.Firefox(service=f)

#driver.get('https://google.com')
firedrive.get('https://google.com')
time.sleep(2)

#fetch the search input box using xpath
user_input = firedrive.find_element(by=By.XPATH, value='/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
user_input.send_keys('CampusX')
#time.sleep(2)

user_input.send_keys(Keys.ENTER)

time.sleep(20)