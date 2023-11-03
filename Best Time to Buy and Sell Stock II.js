function maxProfit(prices) {
    let maxProfit = 0;
    // Start from the second day
    for (let i = 1; i < prices.length; i++) {
        // If the price of the stock has increased compared to the previous day
        if (prices[i] > prices[i - 1]) {
            // Add the difference to maxProfit
            maxProfit += prices[i] - prices[i - 1];
        }
    }
    // Return the total profit
    return maxProfit;
}

// Example usage:
const prices1 = [7, 1, 5, 3, 6, 4];
const prices2 = [1, 2, 3, 4, 5];
const prices3 = [7, 6, 4, 3, 1];

console.log(maxProfit(prices1)); // Output: 7
console.log(maxProfit(prices2)); // Output: 4
console.log(maxProfit(prices3)); // Output: 0


// SOLUTION 2ND

const maxProfit = prices => 
  prices.reduce((profit, price, i, arr) => 
    profit + (i > 0 ? Math.max(0, price - arr[i - 1]) : 0), 0);

// Example usage:
const prices1 = [7, 1, 5, 3, 6, 4];
const prices2 = [1, 2, 3, 4, 5];
const prices3 = [7, 6, 4, 3, 1];

console.log(maxProfit(prices1)); // Output: 7
console.log(maxProfit(prices2)); // Output: 4
console.log(maxProfit(prices3)); // Output: 0
