import json

# requires installs
import requests
from bs4 import BeautifulSoup

url = 'https://www.svt.se/'
response = requests.get(url)

# Check for success
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: extract all links
    for link in soup.find_all('a'):
        print(link.get('href'))
else:
    print(f"Failed to fetch page: {response.status_code}")
