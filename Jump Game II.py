def jump(nums):
    jumps, current_end, current_farthest = 0, 0, 0
    for i in range(len(nums) - 1):
        current_farthest = max(current_farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = current_farthest
    return jumps


# Example usage:
A = [2, 3, 1, 1, 4]
print(jump(A))  # Output: 2
