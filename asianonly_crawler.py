from time import sleep
from bs4 import BeautifulSoup
import urllib
import os
from wget import download
import urllib.parse


def getHostname(url):
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc

url = input("Type asianonly/leakonly url:\n")

req = urllib.request.urlopen(url).read().decode('utf8')
soup = BeautifulSoup(req, 'html.parser')
namedir = soup.find('title').string
imgs_urls = []
hostname = getHostname(url)

if (hostname=='leaksonly.fans'):
    divs = soup.find_all('div', {'itemprop': 'articleBody'})
    figures = divs[0].find_all('figure') 
    for img in figures:
        imgs_urls.append(img.find('img').attrs['src'])
if (hostname=='asianonly.fans'):
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
