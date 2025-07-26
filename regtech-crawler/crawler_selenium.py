from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Setup headless Chrome (runs without opening a window)
options = Options()
options.add_argument("--headless")  # You can remove this if you want to see the browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Load the browser
driver = webdriver.Chrome(options=options)

# List of regulation URLs
urls = [
    'https://peraturan.bpk.go.id/Home/Details/149283/pp-no-1-tahun-2022',
    'https://peraturan.bpk.go.id/Home/Details/146123/pp-no-2-tahun-2021',
    'https://peraturan.bpk.go.id/Home/Details/144211/uu-no-11-tahun-2020',
]

# Crawl each
for url in urls:
    print(f"\n🔗 Opening: {url}")
    driver.get(url)
    time.sleep(2)  # Let JS load

    try:
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        pdf_url = iframe.get_attribute("src")
        print("📎 PDF Link:", pdf_url)

    except Exception as e:
        print("❌ Failed to find title:", e)

# Quit browser
driver.quit()