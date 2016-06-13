import requests
import urllib
from urllib import quote_plus, quote
from urlparse import urljoin
from bs4 import BeautifulSoup
import re

import pdb 

def get_song_lyrics(song_title=None,artist=None):

    #pdb.set_trace()
    if song_title is None:
        song_title = raw_input("Please enter a song title: ")
        artist = raw_input("Who is the artist?")
        
    if artist is not None:

        originalTitle = song_title
        originalArtist = artist

        artist = re.sub("[\.&]","",artist)
        artist = re.sub(" +","-",artist)
        artist = re.sub("Featuring","feat",artist)
        song_title = re.sub("\'","-",song_title)
        song_title = re.sub(" ","-",song_title)

        url2 = "https://www.musixmatch.com/lyrics/" + artist + \
                           "/" + song_title

        print url2

        title = originalArtist + ": " + originalTitle
        
        response = urllib.urlopen(url2).read()
        soup = BeautifulSoup(response,'html.parser')

        checkInstrumental = soup.find_all('h2')

        bInstr = re.findall("([A-Z]\w+)",str(checkInstrumental))


        if re.findall("Instrumental",bInstr[0]):
            print "that's an instrumental track!"
            lyrics=None
            return lyrics, title

        scripts = soup.find_all("script")

        for script in scripts:
            tmp = script.text.split("__mxmState = ")
            if len(tmp)>1:
                data = tmp[1][:-1]
                jsdata = json.loads(data)
                break


        

        try:
            lyrics = jsdata['page']['lyrics']['lyrics']['body']


            # lyrics = re.findall("body\":\"(.*?)\"",response)
            # lyrics = lyrics[0]

            title = originalArtist + ": " + originalTitle
            print "found lyrics on musixmatch!"
            return lyrics, title
        except:
            print "couldn't find on musixmatch"
            pass

    print "searching chartlyrics"
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
        
            print "Couldn't find the lyrics. Try another song."
            return
    return lyrics, title