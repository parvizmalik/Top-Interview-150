def is_happy_number(n):
    def get_next(number):
        """Function to get the sum of the squares of the digits of the number."""
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit * digit
            number //= 10
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

# Test the function with the provided examples
test_cases = [19, 2]
results = [is_happy_number(tc) for tc in test_cases]
print(results)  # Output: [True, False]





# SOLUTION 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def sum_of_squares(num):
    return sum(int(digit)**2 for digit in str(num))

def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
    return n == 1

# Test cases
print(is_happy_number(19))  # Output: True
print(is_happy_number(2))   # Output: False
