class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ind = 0
        # for x in range(len(nums)):
        #     if nums[x] != 0:
        #         nums[x], nums[ind] = nums[ind], nums[x]
        #         ind += 1
        # return nums

        a = 0

        for x in range(len(nums)):
            if nums[x]!=0:
                nums[a] = nums[x]
                a += 1
        for x in range(a, len(nums)):
            nums[x] = 0
        return nums