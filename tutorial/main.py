from bs4 import BeautifulSoup
import requests
import html5lib


url = 'https://www.codewithharry.com/'

#step1: get the html
rq = requests.get(url=url)
html_content = rq.content
# print(html_content)

# step2: parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify) # to prettify the content

# step3: HTMl tree traversal
title = soup.title

# Commonly used types of objects:
        # 1. Tag
        # 2. NavigableString
        # 3. BeautifulSoup
        # 4. Comment
print('soup types is: ', type(soup)) # 1. BeautifulSoup
print(title, 'title type is: ' ,type(title)) # 2. Tag
print(title.string, 'soup types is: ', type(title.string)) # 3. NavigableString

# comment
markup = '<p> <!-- comment goes here!!! --> </p>'
soup2 = BeautifulSoup(markup=markup)
print(type(soup2.p.string))

# Get the title of the HTML page.
title = soup.title

# Get all the paragrapsh from the page
paras = soup.findAll('p')
print(paras)

print('*'*40)
# Get all the anchor tags from the page.
anchors = soup.find_all('a')
print(anchors) # list of anchors

# to get all the links from the page
all_links = set()
for link in anchors:
    if link.get('href') != '#':
        all_links.add(link.get('href'))
print(all_links)

# get the first paragraph from the page
print(soup.find('p'))
print(soup.find('p')['class']) # get classes of any element in the HTML page



# find all the elements with class lead
print(soup.find_all('p', class_ = 'lead'))

# get the text of first paragraph from the page
print(soup.find('p').get_text())
print(soup.get_text())


# find values using id
ids = soup.find(id= 'idGoeshere')
print(ids.contents) # it gives you all the nested/child elements of correspinding 'id'

# .contents = A tag's children are available as a list
# .children = A tag's children are available as a generator

for item in ids.strings:
    print(item)

#.strings
#.stripped_strings

for item in ids.stripped_strings:
    print(item)
    
# to get the parent of the tag
print(ids.parent) # gives you a parent
print(ids.parents) # generator (gives you a whole hierarchy)

for item in ids.parents:
    print(item.name) 

# ids.next_sibling
# ids.previous_sibling
# ids.previous_sibling.previous_sibling


# CSS SELECTORS
ele = soup.select('#loginModel') # id 
print(ele)

ele = soup.select('.modal-footer') # class
print(ele)
