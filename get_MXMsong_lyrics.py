import requests
import urllib
from urllib import quote_plus, quote
from urlparse import urljoin
from bs4 import BeautifulSoup
import re
import json

import pdb
    
def get_MXMsong_lyrics(song_title=None, artist=None):

    originalTitle = song_title
    originalArtist = artist

    artist = re.sub("[\.&!]","",artist)
    artist = re.sub("[ +]","-",artist)
    artist = re.sub("Featuring","feat",artist)
    song_title = re.sub("\'","-",song_title)
    song_title = re.sub(" ","-",song_title)

    url2 = "https://www.musixmatch.com/lyrics/" + artist + \
                       "/" + song_title

    print url2


    response = urllib.urlopen(url2).read()
    soup = BeautifulSoup(response,'html')
    #print soup.prettify()

    #type(soup)
    scripts = soup.findAll('script')
    for script in scripts:
        tmp = script.text.split("__mxmState = ")
        if len(tmp)>1:
            data = tmp[1][:-1]
            jsdata = json.loads(data)
    lyrics = jsdata['page']['lyrics']['lyrics']['body']

    return lyrics, url