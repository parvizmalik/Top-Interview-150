def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = ['' for _ in range(numRows)]
    # rows = [''] * numRows
    current_row = 0
    going_down = False

    for c in s:
        rows[current_row] += c
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)


# Example 1
print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"

# Example 2
print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"

# Example 3
print(convert("A", 1))  # Output: "A"




# SOLUTIONNNNNNNNNNNNNNNNNN 22222222222


def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = {i: '' for i in range(numRows)}
    cur_row = 0
    step = 1

    for c in s:
        rows[cur_row] += c
        if cur_row == 0:
            step = 1
        elif cur_row == numRows - 1:
            step = -1
        cur_row += step

    return ''.join(rows.values())


# Test the function with examples
print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(convert("A", 1))              # Output: "A"
