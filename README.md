This Python script scrapes the top news headlines from a news website (default: The hindu  News) and saves them in a .txt file. It uses the requests and BeautifulSoup libraries.


📂 Files

scape_headlines.py — Python script that performs the web scraping.

headlines.txt — Output file containing the scraped headlines


🔧 Requirements

• Python 3
• requests – for making HTTP requests
• BeautifulSoup (from bs4) – for parsing HTML


🚀 How to Run

1.Install the required libraries (if not already installed):
pip install requests beautifulsoup4

2. Open a terminal in the project folder.

3. Run the script : scrape_headlines.py

4. Headlines will be saved in a file named headlines.txt.


🌐 Default News Source

Website: https://www.thehindu.com/news


🧠 How It Works
• The script sends a GET request to the news website.
• It parses the HTML using BeautifulSoup.
• It looks for headline tags (on the hindu).
• The text of headline is extracted and stored in a file.
