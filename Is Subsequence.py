

def is_subsequence(s: str, t: str) -> bool:
    it = iter(t)
    return all(char in it for char in s)

# Example usage
s1 = "abc"
t1 = "ahbgdc"
print(is_subsequence(s1, t1))  # Output: True

s2 = "axc"
t2 = "ahbgdc"
print(is_subsequence(s2, t2))  # Output: False





# SSSSSSSSSSSSSSSSSSSSSSSOOOOOOOOOOOOOOOOOLLLLLLLLLLLUUUUUUUUUUUUTTTTTTTTTTIIIIIIIIIIIIIIIOOOOOOOOOOOOOOOOONNNNNNNNN 2222222222

def isSubsequence(s, t):
    i, j = 0, 0
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
