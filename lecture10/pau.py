from urllib.request import urlopen

import re
from bs4 import BeautifulSoup

with open("html") as f:
    s = f.readlines()

url = "http://stepic.org/courses"
html = urlopen(url)
soup = BeautifulSoup(html, 'html')
dd = []
for a in soup.find_all("a", href=True):
    dd.append(a["href"])

pp = [p for p in dd if not(p.startswith("/"))]
dd = [re.search(r"^(?:http:\/\/|https:\/\/)([^\/]+)", x).group(1) for x in pp]
print(dd)