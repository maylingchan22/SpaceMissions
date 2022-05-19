from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd

def convert_to_csv(dict_to_convert):
    df = df.DataFrame(dict_to_convert)
    df.to_csv('mission_launches.csv')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://nextspaceflight.com")
# details = driver.find_elements(By.CLASS_NAME, "header-style")
# for x in details:
#     print(x.text)
# organizations = driver.find_elements(By.CSS_SELECTOR, '.rcorners.a.mdl-card__title-text span')
# for x in organizations:
#     print(x.text)
# date = driver.find_elements(By.CSS_SELECTOR, '.mdl-card__supporting-text span')
# for x in date:
#     print(x.text)
location = driver.find_elements(By.CSS_SELECTOR, '.mdl-card__supporting-text span ')
for x in location:
    print(x.text)

#driver.quit()
