

def longest_consecutive(nums):
    num_set = set(nums)
    return max((len({num + i for i in range(len(num_set)) if num + i in num_set}) for num in num_set if num - 1 not in num_set), default=0)

# Example usage
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9





#################################################################################################################################
#################################################################################################################################


def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# Example usage
nums1 = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums1))  # Output: 4

nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longest_consecutive(nums2))  # Output: 9
