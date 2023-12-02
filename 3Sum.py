def three_sum_with_duplicates(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1  # Moving pointers without checking for duplicates
                right -= 1

    return result

# Test the function with the provided example
nums_example = [-1, 0, 1, 2, -1, -4]
three_sum_with_duplicates(nums_example)
