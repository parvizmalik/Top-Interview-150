const intToRoman = (num) => {
  const val = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];

  let romanNumeral = "";

  for (const [i, r] of val) {
    while (num >= i) {
      romanNumeral += r;
      num -= i;
    }
  }

  return romanNumeral;
};

// Test examples
console.log(intToRoman(3)); // Output: "III"
console.log(intToRoman(58)); // Output: "LVIII"
console.log(intToRoman(1994)); // Output: "MCMXCIV"
