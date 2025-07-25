import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = [link['href'] for link in soup.find_all('a')]

print(soup.prettify()) 
print(f"These are the links {links}")