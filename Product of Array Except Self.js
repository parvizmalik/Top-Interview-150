var productExceptSelf = function(nums) {
    let n = nums.length;
    let answer = Array(n).fill(1);  // Correctly initialize the answer array
    let left_product = 1;
    for (let i = 0; i < n; i++) {
        answer[i] = left_product;
        left_product *= nums[i];
    }
    let right_product = 1;
    for (let i = n - 1; i > -1; i--) {  // Correct the loop condition and decrement
        answer[i] *= right_product;
        right_product *= nums[i];
    }
    return answer;
};





//////////////////////////////////////////////////////// more concise and modern JavaScript style




const productExceptSelf = nums => {
    const n = nums.length;
    const answer = new Array(n).fill(1);
    let leftProduct = 1, rightProduct = 1;

    for (let i = 0; i < n; i++) {
        answer[i] = leftProduct;
        leftProduct *= nums[i];
    }

    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return answer;
};

