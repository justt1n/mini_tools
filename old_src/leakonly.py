from time import sleep
from bs4 import BeautifulSoup
import urllib
import os
from wget import download
import urllib.parse
import sys


def getHostname():
    url = sys.argv[1]
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc

    
url = 'https://leaksonly.fans/zhloe-kim%f0%9f%91%98-onlyfans-vietnamese-nude-onlyfans-leaked-70pics/'

#url = input("Nhap url asianonly.fans di fen:")

req = urllib.request.urlopen(url).read().decode('utf8')
soup = BeautifulSoup(req, 'html.parser')
namedir = soup.find('title').string
imgs_urls = []
divs = soup.find_all('div', {'itemprop': 'articleBody'})
figures = divs[0].find_all('figure') 
for img in figures:
    imgs_urls.append(img.find('img').attrs['src'])

print(f"Found {len(imgs_urls)} images!")
sleep(1)
print("Downloading....")


path = os.getcwd()
path = os.path.join(path, namedir + "s")
try:
    print("Creating folder...")
    os.mkdir(path)
except:
    print("Folder exist!")
print("Starting download...")
for img in imgs_urls:
    download(img, out=path)

print("\nDONE!")
