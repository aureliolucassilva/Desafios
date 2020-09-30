# Link -> https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):

    new_list = []
    for item in l:
        if isinstance(item, int):
            new_list.append(item)

    return new_list
