import urllib3
from bs4 import BeautifulSoup
from utils import url


http = urllib3.PoolManager()
r = http.request("GET", url)
html = BeautifulSoup(r.data, "lxml")
"""
print(html.find('input', {'value': '100'}))
print(html.h1)
print(html.h1.text)
print(html.find_all(['h1', 'span']))
print(html.find('span', {'id': {'blue'}, 'class': {'red'}}).get_text())
for child in html.main.children:
    print(child)
for descendant in html.main.descendants:
    print(descendant)
for sibling in  html.section.next_siblings:
    print(sibling)
for sibling in html.find('section', {'id': 'reviews'}).previous_siblings:
    print(sibling)
print(html.find('section').parent.children)
print(html.input.attrs)
for span in html.div.find_all(lambda tag: len(tag.attrs) == 0):
    print(span.text)
"""
print(html.find_all(lambda tag: 'reviews' in tag.attrs.values()))
