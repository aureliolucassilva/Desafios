# Link -> https://www.codewars.com/kata/56269eb78ad2e4ced1000013

import math


def find_next_square(sq):
    root = math.sqrt(abs(sq))

    if math.ceil(root) == root:
        return math.pow(root+1, 2)
    else:
        return -1
