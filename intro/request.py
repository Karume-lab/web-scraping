import requests
from utils import url
from bs4 import BeautifulSoup as bs

try:
	r = requests.get(url)
	"""
	print(r.text)
	for header in r.headers:
		print(f'{header} -> {r.headers[header]}')
	print(r.url)
	print(r.links)
	"""
	soup = bs(r.content, "lxml")
	print(soup.h1)
except Exception as e:
	print(e)
