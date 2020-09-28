import re

def mix(s1, s2):
    # Difference
    differenceString = ''
    repeatList = []

    # Lists
    firstList = re.findall('[a-z]', s1)
    secondList = re.findall('[a-z]', s2)

    # Unordered
    for letter in firstList:
        if letter in secondList and letter not in repeatList:
            repeatList.append(letter)
            firstCount = firstList.count(letter)
            secondCount = secondList.count(letter)

            if firstCount > secondCount and firstCount > 1:
                differenceString += '1:' + letter * firstCount + '/'
            elif secondCount > firstCount and secondCount > 1:
                differenceString += '2:' + letter * secondCount + '/'
            elif secondCount == firstCount and secondCount > 1:
                differenceString += '=:' + letter * secondCount + '/'

        elif letter not in repeatList:
            repeatList.append(letter)
            firstCount = firstList.count(letter)

            if firstCount > 1:
                differenceString += '1:' + letter * firstCount + '/'

    for letter in secondList:
        if letter in firstList and letter not in repeatList:
            repeatList.append(letter)
            firstCount = firstList.count(letter)
            secondCount = secondList.count(letter)

            if secondCount > firstCount and secondCount > 1:
                differenceString += '2:' + letter * secondCount + '/'
            elif firstCount > secondCount and firstCount > 1:
                differenceString += '1:' + letter * secondCount + '/'
            elif firstCount == secondCount and firstCount > 1:
                differenceString += '=:' + letter * secondCount + '/'

        elif letter not in repeatList:
            repeatList.append(letter)
            secondCount = secondList.count(letter)

            if secondCount > 1:
                differenceString += '2:' + letter * secondCount + '/'

    # Pre Order
    orderList = sorted(differenceString.split('/'), key=len, reverse=True)
    del orderList[-1]
    differenceString = ' '.join(orderList) + ' '

    # Final Order
    finalList = []

    for item in orderList:
        # Except
        if item not in differenceString:
            continue

        # Regex
        tempList = re.findall('[0-9]:[a-z]{' + str(len(item) - 2) + '}\s|=:[a-z]{' + str(len(item) - 2) + '}\s', differenceString)
        tempList = sorted(tempList)

        # Clean
        differenceString = re.sub('[0-9]:[a-z]{' + str(len(item) - 2) + '}\s|=:[a-z]{' + str(len(item) - 2) + '}\s', '', differenceString)

        # Add
        for info in tempList:
            finalList.append(info.rstrip())

    # Final
    finalString = '/'.join(finalList)

    return finalString
