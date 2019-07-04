import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup

url = 'https://turnoff.us/feed.xml'
#url = 'https://turnoff.us/geek/the-depressed-developer-2/'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
tag = soup.findAll('img')[0]
#print(tag)
link = tag['src']
name = tag['alt']
name = '-'.join(name.split()).lower()
#print(name)
os.mkdir('./turnoff_Images/')
value = urllib.request.urlretrieve(link, filename = './turnoff_Images/'+ name + '.png')
print("Latest Image :" + name + " saved in turnoff_Images folder")