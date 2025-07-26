import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
}

# List of regulation URLs you want to crawl
urls = [
    'https://peraturan.bpk.go.id/Home/Details/149283/pp-no-1-tahun-2022',
    'https://peraturan.bpk.go.id/Home/Details/146123/pp-no-2-tahun-2021',
    'https://peraturan.bpk.go.id/Home/Details/144211/uu-no-11-tahun-2020',
]

for url in urls:
    print(f"\n🔗 Fetching: {url}")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title
        title_tag = soup.find('h3')
        title = title_tag.text.strip() if title_tag else 'N/A'
        
        print("📘 Title:", title)
    else:
        print(f"❌ Failed to fetch: {response.status_code}")