


const convert = (s, numRows) => {
  if (numRows === 1 || numRows >= s.length) return s;

  const rows = Array.from({ length: numRows }, () => "");
//   const rows = new Array(numRows).fill('');
  let curRow = 0,
    goingDown = false;

  for (const char of s) {
    rows[curRow] += char;
    if (curRow === 0 || curRow === numRows - 1) goingDown = !goingDown;
    curRow += goingDown ? 1 : -1;
  }

  return rows.join("");
};


