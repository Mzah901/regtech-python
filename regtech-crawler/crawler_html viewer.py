import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
}

url = 'https://peraturan.bpk.go.id/Home/Details/149283/pp-no-1-tahun-2022'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())  # See structure first
else:
    print(f"Failed to fetch the page — status code: {response.status_code}")

    