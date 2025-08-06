from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:/Users/asus/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.ajio.com/men-backpacks/c/830201001')
time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
max_scrolls = 50
scroll_attempts = 0

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter+=1
    scroll_attempts += 1

    print(old_height)
    print(new_height)

    if new_height == old_height:
        print("Reached the end of the page")
        break

    if scroll_attempts >= max_scrolls:
        print("Max Scroll attempts reached")
        break

    old_height = new_height

time.sleep(5)
html = driver.page_source

with open('ajio.html', 'w', encoding='utf-8') as f:
    f.write(html)