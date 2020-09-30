# Link -> https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def zero(x=None):
    if x is None:
        return 0
    elif '+' in x:
        return x[0]
    elif '-' in x:
        return -x[0]
    elif '*' in x:
        return 0
    elif '/' in x:
        return 0


def one(x=None):
    if x is None:
        return 1
    elif '+' in x:
        return 1 + x[0]
    elif '-' in x:
        return 1 - x[0]
    elif '*' in x:
        return x[0]
    elif '/' in x:
        return int(1 / x[0])


def two(x=None):
    if x is None:
        return 2
    elif '+' in x:
        return 2 + x[0]
    elif '-' in x:
        return 2 - x[0]
    elif '*' in x:
        return 2 * x[0]
    elif '/' in x:
        return int(2 / x[0])


def three(x=None):
    if x is None:
        return 3
    elif '+' in x:
        return 3 + x[0]
    elif '-' in x:
        return 3 - x[0]
    elif '*' in x:
        return 3 * x[0]
    elif '/' in x:
        return int(3 / x[0])


def four(x=None):
    if x is None:
        return 4
    elif '+' in x:
        return 4 + x[0]
    elif '-' in x:
        return 4 - x[0]
    elif '*' in x:
        return 4 * x[0]
    elif '/' in x:
        return int(4 / x[0])


def five(x=None):
    if x is None:
        return 5
    elif '+' in x:
        return 5 + x[0]
    elif '-' in x:
        return 5 - x[0]
    elif '*' in x:
        return 5 * x[0]
    elif '/' in x:
        return int(5 / x[0])


def six(x=None):
    if x is None:
        return 6
    elif '+' in x:
        return 6 + x[0]
    elif '-' in x:
        return 6 - x[0]
    elif '*' in x:
        return 6 * x[0]
    elif '/' in x:
        return int(6 / x[0])


def seven(x=None):
    if x is None:
        return 7
    elif '+' in x:
        return 7 + x[0]
    elif '-' in x:
        return 7 - x[0]
    elif '*' in x:
        return 7 * x[0]
    elif '/' in x:
        return int(7 / x[0])


def eight(x=None):
    if x is None:
        return 8
    elif '+' in x:
        return 8 + x[0]
    elif '-' in x:
        return 8 - x[0]
    elif '*' in x:
        return 8 * x[0]
    elif '/' in x:
        return int(8 / x[0])


def nine(x=None):
    if x is None:
        return 9
    elif '+' in x:
        return 9 + x[0]
    elif '-' in x:
        return 9 - x[0]
    elif '*' in x:
        return 9 * x[0]
    elif '/' in x:
        return int(9 / x[0])


def plus(y):
    return [y, '+']


def minus(y):
    return [y, '-']


def times(y):
    return [y, '*']


def divided_by(y):
    return [y, '/']
    
