from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from utils import url

html = urlopen(url)
html = BeautifulSoup(html, "lxml")
print(html.find("span", {"class": re.compile("bl*")}))
