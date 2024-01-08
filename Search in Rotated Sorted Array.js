/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let left = 0,
    rig = nums.length - 1;
  while (left <= rig) {
    let mid = left + Math.floor((rig - left) / 2);
    if (target === nums[mid]) {
      return mid;
    }
    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        rig = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (nums[mid] < target && target <= nums[rig]) {
        left = mid + 1;
      } else {
        rig = mid - 1;
      }
    }
  }
  return -1;
};
