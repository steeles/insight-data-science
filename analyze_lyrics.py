import nltk
from nltk.tokenize import WhitespaceTokenizer as wst
import textstat

def analyze_lyrics(lyrics):
    words = lyrics.split()
    song_length = length(words)
    

    return result