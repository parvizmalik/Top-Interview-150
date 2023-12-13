def findRanges(nums):
    result = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
            i += 1
        end = nums[i]
        result.append(str(start) if start == end else str(start) + "->" + str(end))
        i += 1
    return result




def findRanges(nums):
    result = []
    if not nums:
        return result
    
    start = nums[0]
    end = nums[0]

    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            result.append(str(start) if start == end else str(start) + "->" + str(end))
            start = end = num

    result.append(str(start) if start == end else str(start) + "->" + str(end))

    return result
