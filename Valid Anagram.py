from collections import Counter

def isUnicodeAnagram(s, t):
    return Counter(s) == Counter(t)





###################################################################################


def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    hash1, hash2 = {}, {}

    for x in range(len(t)):
      hash1[t[x]] = hash1.get(t[x], 0) + 1
      hash2[s[x]] = hash2.get(s[x], 0) + 1
    return hash1 == hash2

