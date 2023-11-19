def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # Initialize the answer array with 1s

    # Compute left products
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Compute right products and update the answer
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

# Test the function with the provided examples
example1 = [1, 2, 3, 4]
output1 = productExceptSelf(example1)
print(output1)




#  more concise and modern version of the productExceptSelf function in Python by utilizing list comprehensions and the zip function.




def productExceptSelf(nums):
    n = len(nums)
    left_products = [1]
    right_products = [1]

    # Generate left products
    [left_products.append(left_products[-1] * nums[i]) for i in range(n - 1)]

    # Generate right products in reverse
    [right_products.append(right_products[-1] * nums[-1 - i]) for i in range(n - 1)]

    # Reverse right_products for easy pairing with left_products
    right_products.reverse()

    # Combine left and right products
    answer = [l * r for l, r in zip(left_products, right_products)]
    
    return answer

# Test the function
example1 = [1, 2, 3, 4]
output1 = productExceptSelf(example1)
print(output1)
