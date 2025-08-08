import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

driver_path = Service('C:/Users/asus/OneDrive/Desktop/chromedriver.exe')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])

chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(service=driver_path, options=chrome_options)
wait = WebDriverWait(driver, 15)

driver.get('https://www.naukri.com/')
time.sleep(5)

user_input = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
time.sleep(5)

user_input.send_keys('AI Engineer')
time.sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[7]/div/div/div[6]').click()
#submit.send_keys(Keys.Enter)
time.sleep(5)
first_card = []
job_cards = driver.find_elements(By.CSS_SELECTOR, "a.title")
first_card = job_cards[0]
link = first_card.get_attribute("href")
driver.get(link)
print(link)

time.sleep(10)
html = driver.page_source
with open('AI_Engineer_1.html','w', encoding='utf-8') as f:
    f.write(html)
