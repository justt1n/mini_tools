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

    
#url = 'https://asianonly.fans/asian-cosplayer-album-leaked-%e9%b3%97%e9%b1%bc%e9%9c%8f%e5%84%bf-%e7%b2%89%e8%89%b2%e5%85%94%e5%a5%b3%e9%83%8e-cos%e5%90%9b/'

url = input("Nhap url asianonly.fans di fen:")

req = urllib.request.urlopen(url).read().decode('utf8')
soup = BeautifulSoup(req, 'html.parser')
namedir = soup.find('title').string
imgs_urls = []
figures = soup.find_all('li', {'class': 'blocks-gallery-item'})
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
