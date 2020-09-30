# Link -> https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(s):
    words = s.split()
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    return len(shortest)
