# Link ->  https://www.codewars.com/kata/54b72c16cd7f5154e9000457

import re


def decode_bits(bits):
    messageBits = ''

    # Begin and end of message
    a = bits.index('1')
    b = len(bits) - ''.join(list(reversed(bits))).index('1') - 1

    # Zeros
    zeros = re.findall('0+', bits[a:b])

    # 0
    if not zeros:
        messageBits = '.'
        return messageBits

    # 1
    if len(zeros) == 1:
        
        # Ones
        ones = re.findall('1+', bits)
        
        # Time unit 
        timeUnit = min(ones)
        
        # Translation
        if timeUnit == max(ones) and len(timeUnit) == len(zeros[0]):
            bits = re.sub('1{' + str(len(timeUnit)) + '}', '.', bits)
            bits = re.sub('0{' + str(len(timeUnit)) + '}', '', bits)
            messageBits = bits
            return messageBits
        elif len(timeUnit) == len(zeros[0]):
            bits = re.sub('1{' + str(len(timeUnit) * 3) + '}', '-', bits)
            bits = re.sub('1{' + str(len(timeUnit)) + '}', '.', bits)
            bits = re.sub('0{' + str(len(timeUnit)) + '}', '', bits)
            messageBits = bits
            return messageBits
        elif len(timeUnit) > len(zeros[0]):
            timeUnit = zeros[0]
            bits = re.sub('1{' + str(len(timeUnit) * 3) + '}', '-', bits)
            bits = re.sub('1{' + str(len(timeUnit)) + '}', '.', bits)
            bits = re.sub('0{' + str(len(timeUnit)) + '}', '', bits)
        else:
            bits = re.sub('1{' + str(len(timeUnit) * 3) + '}', '-', bits)
            bits = re.sub('1{' + str(len(timeUnit)) + '}', '.', bits)
            bits = re.sub('0{' + str(len(timeUnit) * 3) + '}', '   ', bits)
            messageBits = bits
            return messageBits
        
    # Time unit
    timeUnit = min(zeros)

    # Words
    wordBits = bits.split(timeUnit * 7)

    # Single characters
    chars = []
    for i in wordBits:
        chars.append(i.split(timeUnit * 3))

    # Translation
    for i in chars:
        for j in i:
            j = re.sub('1{' + str(len(timeUnit) * 3) + '}', '-', j)
            j = re.sub('1{' + str(len(timeUnit)) + '}', '.', j)
            j = re.sub('0{' + str(len(timeUnit)) + '}', '', j)
            messageBits += j
            messageBits += ' '
        messageBits += '  '
    
    return messageBits.strip()



def decode_morse(morseCode):
    message = ''
    
    # Morse
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
    
    # Words
    words = morseCode.split('   ')
    
    # Translation
    for i in words:
        letters = i.split(' ')

        for j in letters:
            message += morse_dic[j]

        message += ' '
    
    # Trailing spaces
    message = message.strip()
    
    # False words
    if len(message) == 3:
        message = message.replace(' ', '')
        
    return message
