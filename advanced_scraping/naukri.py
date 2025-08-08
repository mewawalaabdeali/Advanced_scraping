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

top_cards = job_cards[:5]

hrefs = []
for a in top_cards:
    href = a.get_attribute("href")
    print(href)
    if href:
        hrefs.append(href)

for url in hrefs:
    driver.switch_to.new_window('tab')
    driver.get(url)

    time.sleep(7)
    html = driver.page_source
    with open('AI_Engineer_2.html','a', encoding='utf-8') as f:
        f.write(f"\n<!--{url}-->\n")
        f.write(html)
        f.write("\n"+"="*120+ "\n")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

driver.quit()




