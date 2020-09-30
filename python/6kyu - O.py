# Link -> https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    words = sentence.split(" ")
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_sentence = {}

    for word in words:
        for number in numbers:
            if number in word:
                new_sentence[int(number)] = word
                break

    result = ""

    for new_order in sorted(new_sentence.keys()):
        result = result + " " + new_sentence[new_order]

    return result.lstrip()
