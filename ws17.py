import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
#soup = beautifulsoup(r_html)
#title = soup.find('span', 'articletitle').string
#print(title)
