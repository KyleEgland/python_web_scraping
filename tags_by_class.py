#! python3
# This code is based off a tutorial found at:
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# In this file classes and ids will be used to specify which elements are to
# be scraped.
import requests
from bs4 import BeautifulSoup as bs

# Specifying target URL.
target = 'http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html'

# Request the page
page = requests.get(target)

# Pass the file to BeautifulSoup for parsing
soup = bs(page.content, 'html.parser')

# Display the contents of the page as parsed by BeautifulSoup
print('[*] Showing page contents:')
print(soup)

# Use 'find_all' method to search for items by class or id.  The example
# below is searching for any <p> tag that has the class 'outer-text'
print('[*] Find all <p> tags with class "outer-text"')
print(soup.find_all('p', class_='outer-text'))

# Elements can also be found by id
print('[*] Find element by id:')
print(soup.find_all(id="first"))
