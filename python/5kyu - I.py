# Link -> https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    characters = list(string)
    parenthesis = []

    # Empty string
    if string == "":
        return True

    # Order of parenthesis in the string
    for letter in characters:
        if letter == '(':
            parenthesis.append(letter)
        elif letter == ')':
            parenthesis.append(letter)

    # Not valid conditions
    if parenthesis[0] == ')' or parenthesis[-1] == '(':
        return False
    elif len(parenthesis) == 1:
        return False

    # Verification if order is valid
    open_close = 0
    false_pair = 0

    for index in range(len(parenthesis)):
        if index != len(parenthesis) - 1:
            if parenthesis[index] == ')' and parenthesis[index + 1] == '(':
                for side_a in range(index):
                    if parenthesis[side_a] == '(':
                        open_close += 1
                    elif parenthesis[side_a] == ')':
                        open_close -= 1

                if open_close == 0:
                    false_pair += 1
                else:
                    continue

                for side_b in range(len(parenthesis) - 1, index + 1, -1):
                    if parenthesis[side_b] == '(':
                        open_close += 1
                    elif parenthesis[side_b] == ')':
                        open_close -= 1

                if open_close == 0:
                    false_pair += 1

                if false_pair == 2:
                    return False

    open_close = 0

    for individual_parenthesis in parenthesis:
        if individual_parenthesis == '(':
            open_close += 1
        elif individual_parenthesis == ')':
            open_close -= 1

    if open_close == 0:
        return True
    else:
        return False
