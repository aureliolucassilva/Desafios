# Link -> https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def oddTest(element):
    if element % 2 == 0:
        return element
    else:
        return False


def evenTest(element):
    if element % 2 != 0:
        return element
    else:
        return False


def find_outlier(integers):
    odd = 0
    even = 0

    for i in range(0, 3):
        if integers[i] % 2 == 0:
            odd += 1
        else:
            even += 1

    if odd > even:
        outlier = list(filter(evenTest, integers))
    else:
        outlier = list(filter(oddTest, integers))
    
    if not outlier:
        return 0
    else:
        return outlier[0]
