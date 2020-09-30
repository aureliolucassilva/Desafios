# Link -> https://www.codewars.com/kata/54b724efac3d5402db00065e

def decodeMorse(morse_code):
    morse_dic = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '-----': '0',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '...---...': 'SOS',
        '-.-.--': '!',
        '.-.-.-': '.'
    }

    message = ''
    words = morse_code.strip().split('   ')

    for i in words:
        letters = i.split(' ')

        for j in letters:
            message += morse_dic[j]

        message += ' '

    return message.rstrip()
