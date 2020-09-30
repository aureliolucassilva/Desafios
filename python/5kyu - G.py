# link -> https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    # All positive, negative or empty
    if len(arr) == 0:
        return 0
    else:
        all_positive = all(numbers > 0 for numbers in arr)
        all_negative = all(numbers < 0 for numbers in arr)

    if all_positive:
        return sum(arr)
    elif all_negative:
        return 0

    # Other cases
    positive_numbers = {}
    greatest_sum = 0

    for index, number in enumerate(arr):
        if number > 0:
            positive_numbers[index] = number

    for start_index in positive_numbers.keys():
        for end_index in positive_numbers.keys():
            if end_index > start_index:
                generic_sum = sum(arr[start_index:end_index + 1])

                if generic_sum > greatest_sum:
                    greatest_sum = generic_sum

    return greatest_sum
