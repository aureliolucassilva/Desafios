# Link -> https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    n = len(names)
    message = ''

    if n == 0:
        message = 'no one likes this'
    elif n == 1:
        message = names[0] + ' likes this'
    elif n == 2:
        message = names[0] + ' and ' + names[1] + ' like this'
    elif n == 3:
        message = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    elif n >= 4:
        message = names[0] + ', ' + names[1] + ' and ' + str(n - 2) + ' others like this'

    return message
