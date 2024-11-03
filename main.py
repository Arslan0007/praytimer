from bs4 import BeautifulSoup
from fastapi import FastAPI
from urllib.request import urlopen

app = FastAPI(
    title="MyApp",
    version="0.0.1"
)

url = "https://namazvakitleri.diyanet.gov.tr/tr-TR/15845/krakow-icin-namaz-vakti"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
