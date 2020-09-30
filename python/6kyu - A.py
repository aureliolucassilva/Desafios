# Link -> https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    encode = ''
    word = word.lower()

    for i in word:
        x = word.count(i)

        if x > 1:
            encode += ')'
        else:
            encode += '('
    
    return encode
