from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as BS

import pandas as pd

import time

def css_finds(css_selector):
  return driver.find_elements(By.CSS_SELECTOR, css_selector)

def css_find(css_selector):
  return driver.find_element(By.CSS_SELECTOR, css_selector)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_xpath(xpath):
        return driver.find_elements(By.XPATH, xpath)

def find_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('incognito')

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

driver = webdriver.Chrome("./chromedriver.exe", options=options)
driver.get("https://shopping.naver.com/home")
wait = WebDriverWait(driver, 10)


key_word = '여성 봄 자켓'

search = find_xpath("//*/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input")
search.send_keys(f"{key_word}\n")

time.sleep(1.3)

pre_scrollHeight = driver.execute_script("return document.body.scrollHeight") 
interval = 1.3

title = []

time.sleep(2.5)

for _ in range(1, 3):

  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval) 
    curr_scrollHeight = driver.execute_script("return document.body.scrollHeight")

    if pre_scrollHeight == curr_scrollHeight:
        break
    
    pre_scrollHeight = curr_scrollHeight

  serach_title = css_finds("div[class='basicList_title__VfX3c'] > a")

  for i in serach_title:
      title.append(i.text)

  button = find_xpath("/html/body/div/div/div[2]/div[2]/div[3]/div[1]/div[4]/a")
  button.click()

  time.sleep(3)

df = pd.DataFrame(title)

df.to_csv(f"{key_word} 키워드.csv", header=False)

driver.close()

