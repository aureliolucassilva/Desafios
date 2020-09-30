# Link -> https://www.codewars.com/kata/52608f5345d4a19bed000b31

def to_chinese_numeral(n):
    numerals = {
        "-": "负",
        ".": "点",
        0: "零",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
        10: "十",
        100: "百",
        1000: "千",
        10000: "万"
    }

    # Number digits
    single_digits = []
    decimal_digits = []

    if '.' in str(n):
        single_digits = list(str(abs(n)).split('.')[0])
        decimal_digits = list(str(abs(n)).split('.')[1])
    else:
        single_digits = list(str(abs(n)))

    # Chinese numeral
    chinese_numeral = ''

    # 1-9
    if 0 <= abs(n) < 10:
        chinese_numeral += numerals[int(single_digits[0])]

    # 10-19
    elif 10 <= abs(n) < 20:
        chinese_numeral += numerals[10]
        if single_digits[1] != '0':
            chinese_numeral += numerals[int(single_digits[1])]

    # 20-99
    elif 20 <= abs(n) < 100:
        chinese_numeral += numerals[int(single_digits[0])]
        chinese_numeral += numerals[10]

        if single_digits[1] != '0':
            chinese_numeral += numerals[int(single_digits[1])]

    # 100-999
    elif 100 <= abs(n) < 1000:
        if single_digits[1] == '0' and single_digits[2] == '0':
            chinese_numeral += numerals[int(single_digits[0])]
            chinese_numeral += numerals[100]
        else:
            chinese_numeral += numerals[int(single_digits[0])]
            chinese_numeral += numerals[100]
            if single_digits[1] != '0':
                chinese_numeral += numerals[int(single_digits[1])]
                chinese_numeral += numerals[10]
            if single_digits[1] == '0':
                chinese_numeral += numerals[0]
            if single_digits[2] != '0':
                chinese_numeral += numerals[int(single_digits[2])]

    # 1000-9999:
    elif 1000 <= abs(n) < 10000:
        if single_digits[1] == '0' and single_digits[2] == '0' and single_digits[3] == '0':
            chinese_numeral += numerals[int(single_digits[0])]
            chinese_numeral += numerals[1000]
        else:
            chinese_numeral += numerals[int(single_digits[0])]
            chinese_numeral += numerals[1000]
            if single_digits[1] != '0':
                chinese_numeral += numerals[int(single_digits[1])]
                chinese_numeral += numerals[100]
            if single_digits[1] == '0':
                chinese_numeral += numerals[0]
            if single_digits[2] != '0':
                chinese_numeral += numerals[int(single_digits[2])]
                chinese_numeral += numerals[10]
            if single_digits[2] == '0' and single_digits[1] != '0' and single_digits[3] != '0':
                chinese_numeral += numerals[0]
            if single_digits[3] != '0':
                chinese_numeral += numerals[int(single_digits[3])]

    # 10000-99999:
    elif 10000 <= abs(n) < 1000000:
        if single_digits[1] == '0' and single_digits[2] == '0' and single_digits[3] == '0' and single_digits[4] == '0':
            chinese_numeral += numerals[int(single_digits[0])]
            chinese_numeral += numerals[10000]
        elif single_digits[2] == '0' and single_digits[3] == '0' and single_digits[4] == '0':
            chinese_numeral += numerals[int(single_digits[0])]
            chinese_numeral += numerals[10000]
            chinese_numeral += numerals[int(single_digits[1])]
            chinese_numeral += numerals[1000]
        else:
            chinese_numeral += numerals[int(single_digits[0])]
            chinese_numeral += numerals[10000]
            if single_digits[1] != '0':
                chinese_numeral += numerals[int(single_digits[1])]
                chinese_numeral += numerals[1000]
            if single_digits[1] == '0':
                chinese_numeral += numerals[0]
            if single_digits[2] != '0':
                chinese_numeral += numerals[int(single_digits[2])]
                chinese_numeral += numerals[100]
            if single_digits[2] == '0' and single_digits[1] != '0':
                chinese_numeral += numerals[0]
            if single_digits[3] != '0':
                chinese_numeral += numerals[int(single_digits[3])]
                chinese_numeral += numerals[10]
            if single_digits[3] == '0' and single_digits[2] != '0' and single_digits[4] != '0':
                chinese_numeral += numerals[0]
            if single_digits[4] != '0':
                chinese_numeral += numerals[int(single_digits[4])]

    # Decimal
    if len(decimal_digits) > 0:
        chinese_numeral += numerals['.']
        for digit in decimal_digits:
            chinese_numeral += numerals[int(digit)]
    else:
        if list(chinese_numeral)[-1] == numerals[0] and n != 0:
            new_chinese_numeral = list(chinese_numeral)[:len(chinese_numeral) - 1]
            chinese_numeral = "".join(new_chinese_numeral)

    # Negative
    if n < 0:
        chinese_numeral = numerals['-'] + chinese_numeral

    return chinese_numeral
