class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        rig = len(nums)-1

        while left <= rig:
            mid = left+(rig-left)//2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    rig = mid - 1
                else:
                    left = mid+1
            else:
                if target > nums[mid] and target <= nums[rig]:
                    left = mid+1
                else:
                    rig = mid-1
        return -1
