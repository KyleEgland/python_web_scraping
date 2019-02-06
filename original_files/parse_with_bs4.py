#! python3
# This code is based off a tutorial found at:
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# This bit of code builds upon dl_webpage.py in order to demonstrate parsing
# of the HTML.
import requests
from bs4 import BeautifulSoup as bs

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
print('HTML code:\n{}\n'.format(page.content))

# Pass the page downloaded to BeautifulSoup - specifically, the HTML
soup = bs(page.content, 'html.parser')
print('Restructuring HTML printout:\n')
print('{}\n'.format(soup.prettify()))

# Moving through the elements in the HTML
# Select all elements at the top level of the page using the children property
# of soup.  Children returns a list generator so list function is called.
print('List child elements of the HTML document:\n')
print('{}\n'.format(list(soup.children)))
# The above shows that there are two tags at the top level of the page -- the
# initial <!DOCTYPE html> tag and the <html> tag.  There is also a newline
# character in the list.

# Display what each element in the list is
print('Show the "type" of each child element:\n')
print('{}\n'.format([type(item) for item in list(soup.children)]))
# Each item is a BeautifulSoup object.  The first is a Doctype object, which
# contains the information about the type of document.  The second is a
# NavigableString, which represents text found in the HTML document.  The last
# is a Tag object, which contains other nested tags.  This is the most
# important object type and the one dealt with most often.

# Select the html tag and its children by taking the third item in the list.
print('Selecting "html" child from the HTML document.\n')
html = list(soup.children)[2]

# Each item in the list returned by the children property is also a
# BeautifulSoup object, so the children method can be called on html.  Now the
# children inside the html tag can be found.
print('Displaying list of children to "html" tag:\n')
print('{}\n'.format(list(html.children)))
# There are two tags shown in the list from above - head and body - along with
# several newline characters.  The text inside the 'p' tag is what's desired
# for this demonstration.

# The 'body' child is selected in order to get the 'p' tag's text.
print('Selecting "body" tag.\n')
body = list(html.children)[3]

# Now, the contents of the 'p' tag can be grabbed by finding the children of
# the body tag.
print('Displaying ocontents of "body" tag:\n')
print('{}\n'.format(list(body.children)))

# The 'p' tag can now be isolated from the list.
print('Selecting "p" tag.\n')
p = list(body.children)[1]

# The 'get_text' method can be used to extract all of the text inside the tag.
print('Displaying contents of the "p" tag:\n')
print('{}\n'.format(p.get_text()))
