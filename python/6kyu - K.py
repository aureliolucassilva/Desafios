# Link -> https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    a = str(n)
    b = 1
    times = 0

    while len(a) > 1:
        for ch in a:
            b *= int(ch)
        a = str(b)
        b = 1
        times += 1

    return times
