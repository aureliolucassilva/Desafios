def find_even_index(arr):
    # Size array
    i = len(arr)

    # Default
    N = -1

    # Slice array
    for i in range(0, i):
        a = arr[0:i]
        b = arr[i + 1:]

        # Sums
        if sum(a) == sum(b):
            N = i
            break

    return N
