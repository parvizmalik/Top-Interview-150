class Solution {
  isPalindrome(s) {
    // Filter out non-alphanumeric characters and convert to lowercase
    let filteredChars = Array.from(s)
      .filter((char) => /[a-zA-Z0-9]/.test(char))
      .map((char) => char.toLowerCase());

    // Compare the array with its reverse
    return filteredChars.join("") === filteredChars.reverse().join("");
  }
}




class Solution {
  isPalindrome(s) {
    let i = 0,
      j = s.length - 1;

    while (i < j) {
      let a = s[i].toLowerCase();
      let b = s[j].toLowerCase();

      if (/[a-zA-Z0-9]/.test(a) && /[a-zA-Z0-9]/.test(b)) {
        if (a !== b) {
          return false;
        } else {
          i++;
          j--;
          continue;
        }
      }
      i += !/[a-zA-Z0-9]/.test(a) ? 1 : 0;
      j -= !/[a-zA-Z0-9]/.test(b) ? 1 : 0;
    }
    return true;
  }
}
