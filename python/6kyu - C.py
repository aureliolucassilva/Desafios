# Link -> https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    a = str(n)
    b = 0
    
    while len(a) > 1:
        for ch in a:
            b += int(ch)
        a = str(b)
        b = 0
    
    a = int(a)
    return a
