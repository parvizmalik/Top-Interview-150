

# TWO POINTER SOLUTION

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # This line is never reached if the input is valid as per the problem's constraints


# HASH MAP SOLUTION, Time Complexity: O(n), Space Complexity: O(n)

def twoSum(numbers, target):
    hash_table = {}
    for i, number in enumerate(numbers):
        if number in hash_table:
            return [hash_table[number] + 1, i + 1]
        hash_table[target - number] = i
    return []






