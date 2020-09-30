# Link -> https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(n):
    phone_number = ''

    phone_number += '(' + ''.join(list(map(str, n[0:3]))) + ') '
    phone_number += ''.join(list(map(str, n[3:6]))) + '-'
    phone_number += ''.join(list(map(str, n[6:10])))

    return phone_number
