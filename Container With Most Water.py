def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Calculate the area
        width = right - left
        h = min(height[left], height[right])
        area = width * h

        # Update maximum water
        max_water = max(max_water, area)

        # Move the pointers
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example usage
height1 = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]

max_area_1 = max_area(height1) # Output: 49
max_area_2 = max_area(height2) # Output: 1




# SOLUTION 2ND


def max_area(height):
    left, right, max_water = 0, len(height) - 1, 0
    while left < right:
        max_water = max(max_water, (right - left) *
                        min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # Output: 49




