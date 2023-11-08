function jump(nums) {
  let jumps = 0,
    currentEnd = 0,
    currentFarthest = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    currentFarthest = Math.max(currentFarthest, i + nums[i]);
    if (i === currentEnd) {
      jumps++;
      currentEnd = currentFarthest;
    }
  }
  return jumps;
}

// Example usage:
const A = [2, 3, 1, 1, 4];
console.log(jump(A)); // Output: 2
