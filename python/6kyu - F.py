# Link -> https://www.codewars.com/kata/551dc350bf4e526099000ae5

import re


def song_decoder(song):
    # WUB
    lyrics = re.sub('WUB', ' ', song)
    
    # Extra blank spaces
    lyrics = re.sub('\s{2,}', ' ', lyrics)
    
    return lyrics.strip()
