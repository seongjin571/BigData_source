import urllib.request
from bs4 import BeautifulSoup
url='https://askdjango.github.io/lv1/'
req = urllib.request.Request(url) 
 
html =req.text
 
soup = BeautifulSoup(html, 'html.parser')
 
for tag in soup.select('li[class=course]'):
    print(tag.text)


