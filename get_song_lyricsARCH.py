import requests
import urllib
from urllib import quote_plus, quote
from urlparse import urljoin
from bs4 import BeautifulSoup
import re

import pdb 

def get_song_lyrics(song_title=None,*artist):

    #pdb.set_trace()
    if song_title is None:
        song_title = raw_input("Please enter a song title: ")
        artist = raw_input("Who is the artist?")
        
    BASE_URL = "http://www.chartlyrics.com/"
    #queryString = "track.search?q_track=" #chartlyrics would return a soap object if i properly queried it
    searchURL = BASE_URL + "search.aspx?q=" + song_title
    
    fullurl = quote_plus(searchURL, safe="%/:=&?~#!+$,;'@()*[]")
    #fullurl = quote(searchURL, safe="%/:=&?~#!+$,;'@()*[]")

    response = requests.get(fullurl)
    soup = BeautifulSoup(response.text,'lxml')

    tmp = soup.find_all('a')
    song_link = tmp[5];

    # i could also do soup.find('table')

    link = urljoin(BASE_URL, song_link['href'])
    response = requests.get(link);

    soup = BeautifulSoup(response.text,'lxml')
    lyrics_box = soup.find('p')#.text.strip()

    try:
        lyrics = lyrics_box.text.strip()

        title = soup.find('head').find('title').text

        # re.findall("u\'(.*)\\t",

    except:
        if len(artist)<1:
            artist = raw_input("I\'m having trouble finding that song. Who sings it? \n")
        
        try:
artist = re.sub("[\.&]","",artist)
artist = re.sub(" +","-",artist)
artist = re.sub("Featuring","feat",artist)
song_title = re.sub("\'","-",song_title)
song_title = re.sub(" ","-",song_title)

url2 = "https://www.musixmatch.com/lyrics/" + artist + \
                   "/" + song_title

print url2
response = urllib.urlopen(url2).read()
soup = BeautifulSoup(response,'lxml')
tmp = soup.find_all("script")

lyrics = re.findall("body\":\"(.*?)\"",response)
            title=""
        except:
            print "Couldn't find the lyrics. Try another song."
            return
    return lyrics, title