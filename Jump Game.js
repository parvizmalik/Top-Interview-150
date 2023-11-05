function canJump(nums) {
    // The farthest position we can currently reach.
    let farthest = 0;
    
    // Iterate over each index in the array.
    for (let i = 0; i < nums.length; i++) {
        // If the current index is greater than the farthest position we can reach,
        // we cannot proceed, so return false.
        if (i > farthest) {
            return false;
        }
        
        // Update the farthest position we can reach.
        farthest = Math.max(farthest, i + nums[i]);
        
        // If the farthest position we can reach is beyond or at the last index,
        // we can reach the end, so return true.
        if (farthest >= nums.length - 1) {
            return true;
        }
    }
    
    // We have iterated over the array without being able to reach the end,
    // so return false.
    return false;
}

// Example usage:
console.log(canJump([2, 3, 1, 1, 4])); // Output: true
console.log(canJump([3, 2, 1, 0, 4])); // Output: false


// ################################################################################################


const canJump = nums => {
    let farthest = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i > farthest) return false;
        farthest = Math.max(farthest, i + nums[i]);
        if (farthest >= nums.length - 1) return true;
    }
    return false;
};

// Example usage:
console.log(canJump([2, 3, 1, 1, 4])); // Output: true
console.log(canJump([3, 2, 1, 0, 4])); // Output: false
