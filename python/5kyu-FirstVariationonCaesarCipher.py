import math


def moving_shift(s, shift):
    # Alphabet
    upper_alphabet = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "*abcdefghijklmnopqrstuvwxyz"

    code = ''
    for ch in s:
        # Lower
        if ch in lower_alphabet:
            idx = lower_alphabet.index(ch) + shift

            if idx <= 26:
                code += lower_alphabet[idx]
            else:
                while idx > 26:
                    idx -= 26

                code += lower_alphabet[idx]

            shift += 1

        # Upper
        elif ch in upper_alphabet:
            idx = upper_alphabet.index(ch) + shift

            if idx <= 26:
                code += upper_alphabet[idx]
            else:
                while idx > 26:
                    idx -= 26

                code += upper_alphabet[idx]

            shift += 1

        # Special
        else:
            code += ch
            shift += 1

    # Parts
    parts = []
    n = len(code)

    a = math.ceil(len(code) / 5)
    b = 0
    c = a

    # 5x
    for i in range(0, 6):
        parts.append(code[b:c])
        b = c
        c += a

        # Last part
        if c > n:
            c = n

    # Remove empty entries
    parts.remove('')

    return parts


def demoving_shift(s, shift):
    # Alphabet
    upper_alphabet = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "*abcdefghijklmnopqrstuvwxyz"

    decode = ''
    for ch in ''.join(s):
        # Lower
        if ch in lower_alphabet:
            idx = lower_alphabet.index(ch) - shift

            if idx > 0:
                decode += lower_alphabet[idx]
            else:
                while idx < 0:
                    idx += 26
                
                if idx == 0:
                    idx = 26
                
                decode += lower_alphabet[idx]

            shift += 1

        # Upper
        elif ch in upper_alphabet:
            idx = upper_alphabet.index(ch) - shift

            if idx > 0:
                decode += upper_alphabet[idx]
            else:
                while idx < 0:
                    idx += 26
                
                if idx == 0:
                    idx = 26
                
                decode += upper_alphabet[idx]

            shift += 1

        # Special
        else:
            decode += ch
            shift += 1

    return decode
