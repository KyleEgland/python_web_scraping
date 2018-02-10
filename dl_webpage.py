#! python3
# This code is based off a tutorial found at:
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# This bit of code simply does webpage requests.
import requests

# Designating a 'target', not neccessary to do as variable
target = "http://dataquestio.github.io/web-scraping-pages/simple.html"
print('Target: {}'.format(target))

# Request a webpage using the requests.get() method
page = requests.get(target)

# Display the response from that page
# The object obtained is a response object, the below will print the response
print('Response object: {}'.format(page))

# The response object also has a status code, indicating that the page
# downloaded successfully (status code 200)
print('Status code: {}'.format(page.status_code))

# Display the HTML content of the page using content property
print('HTML code:\n{}'.format(page.content))
