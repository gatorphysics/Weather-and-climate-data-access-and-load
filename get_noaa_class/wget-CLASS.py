## Please replace the https link with the link provided by the NOAA CLASS order

from bs4 import BeautifulSoup
import urllib.request
import os
resp = urllib.request.urlopen("https://download.class.ngdc.noaa.gov/download/2602424255/001")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))


for link in soup.find_all('a', href=True):
    a = link['href']
    if(a[-3:]=='.h5'):
        print('https://download.class.ngdc.noaa.gov/download/2602424255/'+a)
        os.system('wget '+'https://download.class.ngdc.noaa.gov/download/2602424255/'+a)
