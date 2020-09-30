# link -> https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    numbers = range(number)
    multiples = []

    for number in numbers:
        if number % 3 == 0 or number % 5 == 0:
            multiples.append(number)

    return sum(multiples)
