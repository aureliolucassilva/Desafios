# Link -> https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    no_zero_array = []
    zeros = []
  
    for element in array:
        if type(element) is str:
            no_zero_array.append(element)
        elif str(element) != '0' and str(element) != '0.0':
            no_zero_array.append(element)
        else:
            zeros.append(0)

    new_array = no_zero_array + zeros

    return new_array
