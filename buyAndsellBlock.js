function maxProfit(prices) {
    let minPrice = Number.POSITIVE_INFINITY;
    let maxProfit = 0;

    for (let price of prices) {
        if (price < minPrice) {
            minPrice = price;
        } else {
            maxProfit = Math.max(maxProfit, price - minPrice);
        }
    }

    return maxProfit;
}

// Test
const prices1 = [7,1,5,3,6,4];
console.log(maxProfit(prices1)); // Output: 5

const prices2 = [7,6,4,3,1];
console.log(maxProfit(prices2)); // Output: 0
