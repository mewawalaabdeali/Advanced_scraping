from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

s = Service("C:/Users/asus/OneDrive/Desktop/chromedriver.exe")

webdriver.Chrome(service=s)
time.sleep(10)
