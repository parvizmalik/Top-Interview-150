const longestConsecutive = (nums) => {
  const numSet = new Set(nums);
  return Math.max(
    ...[...numSet].map((num) =>
      numSet.has(num - 1)
        ? 0
        : 1 +
          [...Array(nums.length).keys()].reduce(
            (acc, _) => (numSet.has(num + acc) ? acc + 1 : acc),
            0
          )
    ),
    0
  );
};

// Example usage
console.log(longestConsecutive([100, 4, 200, 1, 3, 2])); // Output: 4
console.log(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])); // Output: 9


// ##################################################################################################
// ##################################################################################################



function longestConsecutive(nums) {
    if (nums.length === 0) {
        return 0;
    }

    const numSet = new Set(nums);
    let longestStreak = 0;

    for (let num of numSet) {
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentStreak = 1;

            while (numSet.has(currentNum + 1)) {
                currentNum += 1;
                currentStreak += 1;
            }

            longestStreak = Math.max(longestStreak, currentStreak);
        }
    }

    return longestStreak;
}

// Example usage
console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));  // Output: 4
console.log(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));  // Output: 9
