from urllib.request import urlopen

import nltk

url = "http://www.baidu.com"

html = urlopen(url).read()

raw = nltk.clean_html(html)
raw = raw[750:434343]

print(raw)