
function threeSum(nums) {
    nums.sort((a, b) => a - b);
    const result = [];

    for (let i = 0; i < nums.length - 2; i++) {
        // Avoid duplicates for the first number
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            const total = nums[i] + nums[left] + nums[right];

            if (total < 0) {
                left++;
            } else if (total > 0) {
                right--;
            } else {
                result.push([nums[i], nums[left], nums[right]]);

                // Skip duplicates for the second and third numbers
                while (left < right && nums[left] === nums[left + 1]) {
                    left++;
                }
                while (left < right && nums[right] === nums[right - 1]) {
                    right--;
                }

                left++;
                right--;
            }
        }
    }

    return result;
}

// Test the function with the provided example
const numsExample = [-1, 0, 1, 2, -1, -4];
console.log(threeSum(numsExample));




// SOLUTION 2 ##############################################################################


function threeSum(nums) {
    nums.sort((a, b) => a - b);
    const result = [];

    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let [left, right] = [i + 1, nums.length - 1];

        while (left < right) {
            const total = nums[i] + nums[left] + nums[right];

            if (total === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                while (nums[left] === nums[++left]);
                while (nums[right] === nums[--right]);
            } else {
                total < 0 ? left++ : right--;
            }
        }
    }

    return result;
}

// Test the function with the provided example
const numsExample = [-1, 0, 1, 2, -1, -4];
console.log(threeSum(numsExample));

