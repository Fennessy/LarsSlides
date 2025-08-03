# Required installs
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape(url):
    driver = webdriver.Firefox()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup   

def safe_find(soup: BeautifulSoup, name, _class):
    text = soup.find(name, class_=_class)
    if text:
        return text
    else:
        ValueError(f"Could not find {name, _class} for {soup.name}.")

def main():
    url = 'https://www.smhi.se/vader/prognoser-och-varningar/vaderprognos/q/Kinna/Mark/2700839'
    soup = scrape(url)
    text = safe_find(soup, 'span', 'wptS1rOnly')
    print(text.get_text(strip=True))

if __name__ == "__main__":
    main()
    pass


