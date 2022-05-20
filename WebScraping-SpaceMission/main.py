from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import scrapy
import time

url = "https://nextspaceflight.com/launches/past/?search="
response = requests.get(url)
webpage_text = response.text

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
driver.get(url)

organization = []
detail = []
date = []
location = []
soup = BeautifulSoup(webpage_text, 'html.parser')
soup.prettify()
organization.append(soup.find(name="span", style="color: black").get_text(strip=True))
detail.append(soup.find('h5', class_='header-style').get_text(strip=True))
date.append(soup.find("div", class_="mdl-card__supporting-text").get_text(strip=True))
location.append(soup.select("div.mdl-card__supporting-text br")[0].next_sibling.get_text(strip=True))
# print(organization, detail, date, location)

driver.maximize_window()

texts = []
next_pages = driver.find_elements(By.CLASS_NAME, "mdc-button")
for next_page in next_pages:
    text = next_page.text
    texts.append(text)
first_result = next_pages[0]
first_result.click()

time.sleep(20)

new_url = driver.current_url
response2 = requests.get(f'{new_url}')
webpage_text2 = response2.text

status = []
soup2 = BeautifulSoup(webpage_text2, 'html.parser')
soup2.prettify()
p = soup2.find("div", class_="mdl-cell.mdl-cell--6-col-desktop.mdl-cell--12-col-tablet")


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# import pandas as pd
#
# def convert_to_csv(dict_to_convert):
#     df = df.DataFrame(dict_to_convert)
#     df.to_csv('mission_launches.csv')
#
# def get_url(url)
# url = "https://nextspaceflight.com"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get(url)
#
# details = driver.find_elements(By.CLASS_NAME, "header-style")
# for x in details:
#     print(x.text)
# organizations = driver.find_elements(By.CSS_SELECTOR, '.rcorners.a.mdl-card__title-text span')
# for x in organizations:
#     print(x.text)
# date = driver.find_elements(By.CSS_SELECTOR, '.mdl-card__supporting-text span')
# for x in date:
#     print(x.text)


# previews = driver.find_elements(By.CLASS_NAME, "mdl-cell mdl-cell--6-col")
# for preview in previews:
#     organization = [x.text for x in preview.find_elements(By.XPATH, "./html/body/div/div/main/div/section[1]/div/div[1]/div/div[1]/div/div/span")]
#     details = preview.find_elements(By.XPATH, "./html/body/div/div/main/div/section[1]/div/div[1]/div/h5")
#     date = preview.find_elements(By.XPATH, ".//*[@id='localized356']")
#     location = preview.find_elements(By.XPATH, "./html/body/div/div/main/div/section[1]/div/div[1]/div/div[3]/div[1]/text()")
#     print(organization)

#driver.quit()
