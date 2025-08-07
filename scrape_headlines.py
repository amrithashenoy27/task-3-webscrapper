import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/news/"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
headlines = soup.find_all("h3")
unique_headlines = set()

for headline in headlines:
    text = headline.get_text(strip=True)
    if text:
        unique_headlines.add(text)

with open("headlines.txt", "w",encoding="utf-8") as file:
    for headline in unique_headlines:
        file.write(headline + "\n")

print("Headlines saved to headlines.txt")