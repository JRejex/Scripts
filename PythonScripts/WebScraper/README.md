## Web Scrapers
Process a target website and extract key information and suspicious content
```
Tools:
- WebScraper.py 
```
Web scraper will crawl target website utilizing BeautifulSoup html parser, and regex.\ Then save the following output information to a text file for referencing. 
- page-title
- page-links
- images

Modify the following variables within the script prior to execution and change to target site:
```
url = 'https://github.com/JRejex/' # CHANGE TO TARGET URL
base = 'https://github.com' # CHANGE TO TARGET URL BASE
```

Example Output:
![WebScraper_Screenshot](https://user-images.githubusercontent.com/42547204/196287503-8612d26a-076c-495e-8ce0-b77958eddffc.JPG)
