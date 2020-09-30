# Link -> https://www.codewars.com/kata/5541f58a944b85ce6d00006a

def productFib(prod):
    f1 = 0
    f2 = 1
    f3 = 1

    while f1 * f2 != prod or f2 * f3 != prod:
        if f1 * f2 < prod and f2 * f3 < prod:
            f1 = f2
            f2 = f3
            f3 = f1 + f2
        else:
            if f1 * f2 == prod:
                return [f1, f2, True]
            elif f2 * f3 == prod:
                return [f2, f3, True]
            elif f1 * f2 < prod < f2 * f3:
                return [f2, f3, False]
