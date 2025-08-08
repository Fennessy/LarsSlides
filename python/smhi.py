import os
import re
import json

# Required installs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException


def scrape(url):
    options = Options()
    options.headless = True  # Run in headless mode
    try:
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        html = driver.page_source
    except WebDriverException as e:
        raise RuntimeError(f'Error loading page: {e}')
    finally:
        driver.quit()
    return BeautifulSoup(html, 'html.parser')


def safe_find(soup: BeautifulSoup, name, class_name):
    element = soup.find(name, class_=class_name)
    if element:
        return element
    raise ValueError(f"Could not find <{name} class='{class_name}'> in {soup.name}.")


def clean_summary(text: str) -> str:
    cleaned = re.sub(r'Klockan \d{1,2} ', '', text).strip()
    return cleaned.capitalize()


def save_json(data: dict, filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    url = 'https://www.smhi.se/vader/prognoser-och-varningar/vaderprognos/q/Skene/Mark/2677749'
    output_path = 'SlidesV2/src/lib/smhi/smhi.json'

    soup = scrape(url)
    span = safe_find(soup, 'span', 'wptSrOnly')
    img = safe_find(soup, 'img', '_weatherIcon_sq1e0_1 _weatherSymbol_103ri_159')

    weather_desc = clean_summary(span.get_text())
    icon = 'https://www.smhi.se' + img.get('src')

    dictionary = {
        'weather_desc' : weather_desc,
        'icon' : icon
    }

    save_json(dictionary, output_path)
    print(f'Saved to {output_path}')


if __name__ == '__main__':
    main()
