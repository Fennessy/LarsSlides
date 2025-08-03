import json
import os

# Required installs
import requests
from bs4 import BeautifulSoup

from svt import scrape


def main():
    url = 'https://www.smhi.se/vader/prognoser-och-varningar/vaderprognos/q/Kinna/Mark/2700839'
    soup = scrape(url)
    text = soup.find('div', class_='_forecastCard_103ri_126')
    print(soup)

if __name__ == "__main__":
    #main()
    pass

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://example.com/your-target-url")

soup = BeautifulSoup(driver.page_source, 'html.parser')
el = soup.find("span", class_="wptSrOnly")
if el:
    print(el.get_text(strip=True))
else:
    print("Element not found.")

driver.quit()

