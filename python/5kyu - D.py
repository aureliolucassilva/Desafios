# Link -> https://www.codewars.com/kata/550f22f4d758534c1100025a

import re

def dirReduc(arr):
    path = '#'.join(arr)

    while re.search("NORTH#+SOUTH", path) or re.search("SOUTH#+NORTH", path) or re.search("WEST#+EAST", path) or re.search("EAST#+WEST", path):
        path = re.sub("NORTH#+SOUTH", '', path)
        path = re.sub("WEST#+EAST", '', path)
        path = re.sub("SOUTH#+NORTH", '', path)
        path = re.sub("EAST#+WEST", '', path)

    cleanPath = path.split('#')

    while '' in cleanPath:
        cleanPath.remove('')

    return cleanPath
