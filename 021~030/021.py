# 021.py
import time
import requests
from bs4 import BeautifulSoup

html = requests.get('https://ridibooks.com/category/bestsellers/2200').text

soup = BeautifulSoup(html, 'html.parser')

tag_list = []
start = time.clock()
print('- Start Parsing -')

for tag in soup.select('.title_link > .title_text') :
    if tag :
        x = tag.text
        tag_list.append(x.strip())

print('걸린 시간 : ' + str((time.clock() - start)))
print('- Finish Parsing -')

k = 0

with open('ridi.csv', 'w') as f :
    for tag in tag_list :
        k += 1
        f.write(str(k) + '. ' + tag + '\n')
