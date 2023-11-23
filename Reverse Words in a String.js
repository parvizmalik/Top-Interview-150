

var reverseWords = function (s) {
  return s
    .trim()
    .split(" ")
    .filter((word) => word.length > 0)
    .reverse()
    .join(" ");
};



//////////////////////////////////////////////////////////////////

function reverseWords(s) {
  let words = [],
    word = "";
  for (let i = 0; i <= s.length; i++) {
    if (s[i] !== " " && i !== s.length) {
      word += s[i];
    } else if (word.length > 0) {
      words.push(word);
      word = "";
    }
  }
  return words.reverse().join(" ");
}

// Example usage
let example = "the sky is blue";
let output = reverseWords(example);
console.log(output);
