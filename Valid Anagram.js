function isAnagram(s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const countS = {};
  const countT = {};

  for (let i = 0; i < s.length; i++) {
    countS[s[i]] = (countS[s[i]] || 0) + 1;
    countT[t[i]] = (countT[t[i]] || 0) + 1;
  }

  for (let char in countS) {
    if (countS[char] !== countT[char]) {
      return false;
    }
  }

  return true;
}


// #########################################################################


function isAnagram(s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const charCount = new Map();

  for (let i = 0; i < s.length; i++) {
    charCount.set(s[i], (charCount.get(s[i]) || 0) + 1);
    charCount.set(t[i], (charCount.get(t[i]) || 0) - 1);
  }

  for (let count of charCount.values()) {
    if (count !== 0) {
      return false;
    }
  }

  return true;
}
