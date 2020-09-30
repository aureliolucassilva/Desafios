# Link -> https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    words = sentence.split()
    spin = ''

    for i in words:
        if len(i) >= 5:
            spin += i[::-1] + ' '
        else:
            spin += i + ' '

    spin = spin.rstrip()

    return spin
