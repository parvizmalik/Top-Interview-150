function twoSum(numbers, target) {
  let left = 0,
    right = numbers.length - 1;

  while (left < right) {
    let currentSum = numbers[left] + numbers[right];
    if (currentSum === target) {
      return [left + 1, right + 1];
    } else if (currentSum < target) {
      left++;
    } else {
      right--;
    }
  }

  return []; // This line is never reached if the input is valid as per the problem's constraints
}




function twoSum(numbers, target) {
  let hashTable = {};

  for (let i = 0; i < numbers.length; i++) {
    let complement = target - numbers[i];
    if (hashTable[complement] !== undefined) {
      return [hashTable[complement] + 1, i + 1];
    }
    hashTable[numbers[i]] = i;
  }

  return [];
}




function twoSum(numbers, target) {
  let hashTable = new Map();

  for (let i = 0; i < numbers.length; i++) {
    let number = numbers[i];
    if (hashTable.has(number)) {
      return [hashTable.get(number) + 1, i + 1];
    }
    hashTable.set(target - number, i);
  }

  return [];
}








