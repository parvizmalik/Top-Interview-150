from typing import List

class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle the case where k >= n
        self.reverse(nums, 0, n - 1)  # Reverse the entire array
        self.reverse(nums, 0, k - 1)  # Reverse the first k elements
        self.reverse(nums, k, n - 1)  # Reverse the remaining n - k elements

# Example usage:
solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]




def rotate(nums,k):
    n = len(nums)
    k = k % n 

    for i in range(k):
        previous = nums[n-1]
        # n -= 1 
        for j in range(len(nums)):
            nums[j], previous = previous, nums[j]
    return nums
print(rotate([1,2,3,4], 2))




# SOLUTION METHOD 3 ----  Using Extra Space
def rotate(nums, k):
    n = len(nums)
    k = k % n  # Handle the case where k >= n
    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = nums[i]
    nums[:] = rotated  # Copy the rotated array back to nums

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]





