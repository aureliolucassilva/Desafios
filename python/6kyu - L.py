# Link -> https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(starr, k):
    if len(starr) == 0 or k > len(starr) or k <= 0:
        return ""
    else:
        longest = ""
        long_string = ""

        for string in starr[0:len(starr) - k + 1]:
            long_string = string
            index = starr.index(string)

            for idx in range(1, k):
                long_string = long_string + starr[index + idx]

            if len(long_string) > len(longest):
                longest = long_string

    return longest
