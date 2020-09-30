# Link -> https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    position = ''

    for ch in text.lower():
        if ch in alphabet:
            position += str(alphabet.index(ch) + 1) + ' '

    return position.rstrip()
