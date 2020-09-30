# Link -> https://www.codewars.com/kata/54a91a4883a7de5d7800009c


def increment_string(string):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    number_to_increment = []

    # Finding the numbers
    for char in list(string):
        if char in numbers:
            number_to_increment.append(char)
        else:
            number_to_increment = []

    # Index of the first number
    number_substring = ''.join(number_to_increment)
    index = string.find(number_substring)

    # Incrementing the string
    if len(number_to_increment) == 0:
        return string + "1"
    else:
        new_number = int(''.join(number_to_increment)) + 1
        new_string = string[:index] + str(new_number).zfill(len(number_to_increment))

        return new_string
