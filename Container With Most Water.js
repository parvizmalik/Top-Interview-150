var maxArea = function (height) {
  let left = 0,
    right = height.length - 1,
    max_water = 0;
  while (right > left) {
    let width = right - left;
    let l = Math.min(height[left], height[right]),
      cur_water = width * l;
    max_water = Math.max(cur_water, max_water);

    if (height[left] > height[right]) {
      right--;
    } else {
      left++;
    }
  }
  return max_water;
};




// 2ND SOLUTIONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN


const maxArea = (height) => {
  let left = 0,
    right = height.length - 1,
    maxWater = 0;
  while (left < right) {
    const width = right - left;
    maxWater = Math.max(
      maxWater,
      width * Math.min(height[left], height[right])
    );
    height[left] > height[right] ? right-- : left++;
  }
  return maxWater;
};
