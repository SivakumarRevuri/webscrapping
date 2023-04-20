from urllib.request import urlopen

URL = 'http://pythonscraping.com/pages/page1.html'
html = urlopen(url = URL)

print(html.read())

# urllib: is a standard python library
