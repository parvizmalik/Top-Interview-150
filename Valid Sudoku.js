function isValidSudoku(board) {
    const rows = {};
    const cols = {};
    const boxes = {};

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const num = board[i][j];
            if (num === ".") continue;

            // Compute box key
            const boxKey = `${Math.floor(i / 3)}-${Math.floor(j / 3)}`;

            // Initialize the sets if they don't exist
            rows[i] = rows[i] || new Set();
            cols[j] = cols[j] || new Set();
            boxes[boxKey] = boxes[boxKey] || new Set();

            // Check for duplicates in rows, columns, and boxes
            if (rows[i].has(num) || cols[j].has(num) || boxes[boxKey].has(num)) {
                return false;
            }

            // Add the number to the row, column, and box sets
            rows[i].add(num);
            cols[j].add(num);
            boxes[boxKey].add(num);
        }
    }

    return true;
}

// Example usage
const board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
];

console.log(isValidSudoku(board)); // Output: true
