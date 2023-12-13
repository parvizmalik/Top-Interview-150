function findRanges(nums) {
    const result = [];
    for (let i = 0; i < nums.length; i++) {
        const start = nums[i];
        let end = start;
        while (i + 1 < nums.length && nums[i + 1] === nums[i] + 1) {
            end = nums[i + 1];
            i++;
        }
        result.push(start === end ? `${start}` : `${start}->${end}`);
    }
    return result;
}

// Example usage
const nums1 = [0, 1, 2, 4, 5, 7];
const nums2 = [0, 2, 3, 4, 6, 8, 9];

console.log(findRanges(nums1)); // ["0->2", "4->5", "7"]
console.log(findRanges(nums2)); // ["0", "2->4", "6", "8->9"]


// $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
// $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




function findRanges(nums) {
    const result = [];
    let i = 0;
    while (i < nums.length) {
        const start = nums[i];
        while (i < nums.length - 1 && nums[i] + 1 === nums[i + 1]) {
            i++;
        }
        const end = nums[i];
        result.push(start === end ? `${start}` : `${start}->${end}`);
        i++;
    }
    return result;
}


