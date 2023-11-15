function isSubsequence(s, t) {
  let i = 0,
    j = 0;
  while (j < t.length) {
    if (i < s.length && s[i] === t[j]) {
      i++;
    }
    j++;
  }
  return i === s.length;
}

// Example usage
const s1 = "abc";
const t1 = "ahbgdc";
console.log(isSubsequence(s1, t1)); // Output: true


// SSSSSSSSSSSSSSSSSSSSSSSOOOOOOOOOOOOOOOOOLLLLLLLLLLLUUUUUUUUUUUUTTTTTTTTTTIIIIIIIIIIIIIIIOOOOOOOOOOOOOOOOONNNNNNNNN 2222222222

function is_subsequence(s, t) {
    let index = 0;
    return [...s].every(char => {
        index = t.indexOf(char, index);
        if (index === -1) return false;
        index++;
        return true;
    });
}

// Example usage
const s2 = "abc";
const t2 = "ahbgdc";
console.log(is_subsequence(s2, t2));  // Output: true


// SSSSSSSSSSSSSSSSSSSSSSSOOOOOOOOOOOOOOOOOLLLLLLLLLLLUUUUUUUUUUUUTTTTTTTTTTIIIIIIIIIIIIIIIOOOOOOOOOOOOOOOOONNNNNNNNN 2222222222

function isSubsequence(s, t) {
    let pos = 0;
    return [...s].reduce((isSubseq, char) => {
        pos = t.indexOf(char, pos) + 1;
        return isSubseq && pos > 0;
    }, true);
}

// Example usage
const s = "abc";
const t = "ahbgdc";
console.log(isSubsequence(s, t));  // Output: true
