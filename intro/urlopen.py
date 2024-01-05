from urllib.request import urlopen
from utils import url

html = urlopen(url)
print(html.read())
