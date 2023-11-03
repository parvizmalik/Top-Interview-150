def maxProfit(prices):
    maxProfit = 0
    # Start from the second day
    for i in range(1, len(prices)):
        # If the price of the stock has increased compared to the previous day
        if prices[i] > prices[i - 1]:
            # Add the difference to maxProfit
            maxProfit += prices[i] - prices[i - 1]
    # Return the total profit
    return maxProfit

# Example usage:
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]

print(maxProfit(prices1)) # Output: 7
print(maxProfit(prices2)) # Output: 4
print(maxProfit(prices3)) # Output: 0



# SOLUTION 2ND 

def maxProfit(prices):
    return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))

# Example usage:
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]

print(maxProfit(prices1)) # Output: 7
print(maxProfit(prices2)) # Output: 4
print(maxProfit(prices3)) # Output: 0
