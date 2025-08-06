from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.service import Service

s = Service("C:/Users/asus/OneDrive/Desktop/chromedriver.exe")
#f = Service("C:/Users/asus/OneDrive/Desktop/geckodriver.exe")

driver = webdriver.Chrome(service=s)
#firedrive = webdriver.Firefox(service=f)

driver.get('https://www.bing.com')
#firedrive.get('https://google.com')
time.sleep(2)

#fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH, value='//*[@id="sb_form_q"]')
user_input.send_keys('CampusX')
time.sleep(2)
user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH, value='//*[@id="b_results"]/li[1]/div[2]/div/h2/a')
link.click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[-1])
link2 = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/section[2]/a[8]')
link2.click()




time.sleep(20)