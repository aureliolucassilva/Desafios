# Link -> https://www.codewars.com/kata/59473c0a952ac9b463000064

def alphabet_war(fight):
    order = {
        'left-right': {'w': 'm',
                       'p': 'q',
                       'b': 'd',
                       's': 'z'},

        'right-left': {'z': 's',
                       'm': 'w',
                       'd': 'b',
                       'q': 'p'}
    }

    leftSide = {
        'w': 4,  # -> 119
        'p': 3,  # -> 112
        'b': 2,  # -> 98
        's': 1,  # -> 115
        't': 0
    }

    rightSide = {
        'm': 4,  # -> 109
        'q': 3,  # -> 113
        'd': 2,  # -> 100
        'z': 1,  # -> 122
        'j': 0
    }

    newFight = ''

    for i in range(0, len(fight)):
        # 0
        if fight[i] in ['t', 'j'] or len(fight) == 1:
            newFight += fight[i]
            continue
        # 1
        if i == 0:
            # t
            if fight[i + 1] == 't':
                if fight[i] in rightSide:
                    newFight += order['right-left'][fight[i]]
                else:
                    newFight += fight[i]
            # j
            elif fight[i + 1] == 'j':
                if fight[i] in leftSide:
                    newFight += order['left-right'][fight[i]]
                else:
                    newFight += fight[i]
            # Neutral
            else:
                newFight += fight[i]
        # 2
        elif i == len(fight) - 1:
            # t
            if fight[i - 1] == 't':
                if fight[i] in rightSide:
                    newFight += order['right-left'][fight[i]]
                else:
                    newFight += fight[i]
            # j
            elif fight[i - 1] == 'j':
                if fight[i] in leftSide:
                    newFight += order['left-right'][fight[i]]
                else:
                    newFight += fight[i]
            # Neutral
            else:
                newFight += fight[i]
        # 3
        elif(fight[i + 1] == 't' and fight[i - 1] != 'j') or (fight[i - 1] == 't' and fight[i + 1] != 'j'):
            # t
            if fight[i] in rightSide:
                newFight += order['right-left'][fight[i]]
            else:
                newFight += fight[i]
        # 4
        elif (fight[i + 1] == 'j' and fight[i - 1] != 't') or (fight[i - 1] == 'j' and fight[i + 1] != 't'):
            # j
            if fight[i] in leftSide:
                newFight += order['left-right'][fight[i]]
            else:
                newFight += fight[i]
        # 5
        else:
            newFight += fight[i]

    leftPower = 0
    rightPower = 0

    for item in newFight:
        if item in leftSide:
            leftPower += leftSide[item]
        elif item in rightSide:
            rightPower += rightSide[item]

    if leftPower > rightPower:
        return "Left side wins!"
    elif rightPower > leftPower:
        return "Right side wins!"
    else:
        return "Let's fight again!"
