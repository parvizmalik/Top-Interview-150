

def intToRoman(num):
    # Mapping of Roman numerals and their corresponding values
    val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    roman_numeral = ""
    for i, r in val:
        # Append the corresponding numeral while reducing the number
        while num >= i:
            roman_numeral += r
            num -= i

    return roman_numeral


# Test the function
print(intToRoman(3))    # Output: "III"
print(intToRoman(58))   # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"






# SOLUTION 2////////////////////////////////////////////////////////////////////////////////


def intToRoman(num):
    val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    return ''.join([r * (num // i) + (num := num % i and num or num) for i, r in val if num >= i])


# Test the function
print(intToRoman(3))    # Output: "III"
print(intToRoman(58))   # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"


# SOLUTION 3///////////////////////////////////////////////////////////////////////////////////


def intToRoman(num):
    val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    roman_numeral = ""
    for i, r in val:
        count = num // i
        roman_numeral += r * count
        num -= i * count

    return roman_numeral


# Test the function
print(intToRoman(3))    # Output: "III"
print(intToRoman(58))   # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"
