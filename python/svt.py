import json
import os

# requires installs
import requests

def scrape(link):
    try:
        response = requests.get(link, headers={"User-Agent": "Mozilla/5.0"}, timeout=1)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed: {response.status_code} for {link}")
    except requests.exceptions.Timeout:
        print(f"Timeout occurred for {link}")
        # Custom behavior here: retry, return None, log, etc.
    except requests.RequestException as e:
        print(f"Request error for {link}: {e}")
    
    return None


def getUrls(base_url):
    soup = scrape(base_url)
    urls = []
    section = soup.find('section', class_='MostImportant__root___KEF4K MostImportant__hideInMobile___D4hDD')
    if section:
        items = section.find_all('a', class_='MostImportant__link___ZTNTw')
        for item in items:
            relative_url = item.get('href')
            if relative_url:
                full_url = base_url + relative_url if relative_url.startswith("/") else relative_url
                urls.append(full_url)
    else:
        print("Could not find news section.")
    return urls

def getSmallNews(link):
    soup = scrape(link)
    title, published, body = None, None, ""
    article = soup.find('article', class_='TextArticle__root___ov1YN')
    if not article:
        print(f"Article not found at {link}")
        return {"title": None, "published": None, "body": None}

    title = article.find('h1', class_='TextArticle__heading___tebP2').get_text(strip=True)
    published = article.find('section', class_='ArticleTopTimestamp__root___ST1S2').get_text(strip=True)
    corpus = article.find('div', class_='InlineText__root___g8u-1')
    body = '\n'.join(p.get_text(strip=True) for p in corpus.find_all(['p', 'h2', 'h3']) if p.get_text(strip=True))

    return {
        "title": title,
        "published": published,
        "body": body
    }


def main():
    url = 'https://www.st.se'
    urls = getUrls(url)

    all_news = [getSmallNews(sub_url) for sub_url in urls]

    output_path = "SlidesV2/src/lib/svt_news/svt_news.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_news, f, ensure_ascii=False, indent=2)

 
if __name__ == '__main__':
    main()
