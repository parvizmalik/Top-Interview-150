class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                nums = board[i][j]
                if nums == ".":
                    continue
                if nums in rows[i] or nums in cols[j] or nums in boxes[(i//3, j//3)]:
                    return False
                cols[j].add(nums)
                rows[i].add(nums)
                boxes[(i//3, j//3)].add(nums)
        return True
    
# SOLUTION 222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222


def isValidSudoku(board):
    # Create sets to track seen numbers in rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                # Calculate box index
                box_index = (i // 3) * 3 + j // 3

                # Check if the number is already in the current row, column, or box
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                # Add the number to the respective row, column, and box
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

    return True

# Example usage
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board1)) # Output: true
print(isValidSudoku(board2)) # Output: false
