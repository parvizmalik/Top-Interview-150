
function isHappyNumber(n) {
    function getNext(number) {
        return String(number)
            .split('')
            .reduce((sum, digit) => sum + Math.pow(parseInt(digit, 10), 2), 0);
    }

    const seen = new Set();
    while (n !== 1 && !seen.has(n)) {
        seen.add(n);
        n = getNext(n);
    }

    return n === 1;
}

console.log(isHappyNumber(19)); // Output: true



// SOLUTION 2 ----------------------###################################???????


function isHappyNumber(n) {
    function getSumOfSquares(num) {
        let sum = 0;
        while (num > 0) {
            let digit = num % 10;
            sum += digit * digit;
            num = Math.floor(num / 10);
        }
        return sum;
    }

    const seen = new Set();
    while (n !== 1 && !seen.has(n)) {
        seen.add(n);
        n = getSumOfSquares(n);
    }

    return n === 1;
}

// Test the function with the provided examples
console.log(isHappyNumber(19)); // true
console.log(isHappyNumber(2));  // false
