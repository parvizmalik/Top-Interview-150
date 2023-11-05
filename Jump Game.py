

def can_jump(nums):
    # Create an array to keep track of which positions are reachable.
    # Initialize the first position as True since we start there.
    n = len(nums)
    dp = [False] * n
    dp[0] = True
    
    # Go through each position in the array.
    for i in range(n):
        # If the current position is not reachable, skip it.
        if not dp[i]:
            continue
        
        # From the current position, update the reachability of the next positions.
        for j in range(i + 1, min(i + nums[i] + 1, n)):
            dp[j] = True
        
        # If the last position is reachable, return True.
        if dp[-1]:
            return True
    
    # Return whether the last position is reachable.
    return dp[-1]

# Example usage:
print(can_jump([2,3,1,1,4]))  # Output: True
print(can_jump([3,2,1,0,4]))  # Output: False


################################################################################################################


# IN MORE CONCISE WAY


def can_jump(nums):
    farthest = 0
    for i, num in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + num)
        if farthest >= len(nums) - 1:
            return True
    else:
        return False

# Example usage:
print(can_jump([2,3,1,1,4]))  # Output: True
print(can_jump([3,2,1,0,4]))  # Output: False
