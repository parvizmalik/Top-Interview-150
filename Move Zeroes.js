var moveZeroes = function(nums) {
    let a = 0;
    for (let i=0; i<nums.length;i++ ){
        if (nums[i]!==0){
            [nums[i], nums[a]]=[nums[a], nums[i]]
            a++;
        }
        
    }
    return nums;
};