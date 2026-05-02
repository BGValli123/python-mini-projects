import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # ✅ REQUIRED

print("="*50)
print("🌐 Simple Web Scraper")
print("="*50)

url = input("Enter website URL: ")

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print("\n🔍 Page Title:")
    print(soup.title.string)

    print("\n🔗 All Links:\n")

    links = soup.find_all("a")

    # ✅ Correct indentation
    for i, link in enumerate(links[:10]):
        full_link = urljoin(url, link.get('href'))
        print(f"{i+1}. {full_link}")

except Exception as e:
    print("❌ Error:", e)
