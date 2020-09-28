import re


def song_decoder(song):
    # WUB
    lyrics = re.sub('WUB', ' ', song)
    
    # Extra blank spaces
    lyrics = re.sub('\s{2,}', ' ', lyrics)
    
    return lyrics.strip()
