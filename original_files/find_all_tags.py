#! python3
# This code is based off a tutorial found at:
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# This bit of code builds upon parse_with_bs4.py in order to demonstrate
# parsing of the HTML in a more simplified fashio.
import requests
from bs4 import BeautifulSoup as bs

# Designating a 'target', not neccessary to do as variable
target = "http://dataquestio.github.io/web-scraping-pages/simple.html"
print('[*] Target: {}'.format(target))

# Request a webpage using the requests.get() method
print('[*] Requesting page.')
page = requests.get(target)

# The response object also has a status code, indicating that the page
# downloaded successfully (status code 200)
print('[*] Status code: {}'.format(page.status_code))

# Pass the page downloaded to BeautifulSoup - specifically, the HTML
soup = bs(page.content, 'html.parser')

# Find all of the paragraph, 'p', tags.
print('[*] Find all <p> tags:')
print(soup.find_all('p'))
# The 'find_all' returns a list.  Loop through list or use list indexing to
# extract the text.
print('[*] Grab just text from <p> tag:')
print(soup.find_all('p')[0].get_text())

# The first instance of a tag can be found by using the 'find' method.  This
# returns a BeautifulSoup object:
print('[*] Get first instance of <p> tag:')
print(soup.find('p'))
