def isIsomorphic(s, t):
    hash_m = {}
    hash_m2 = {}

    for a, b in zip(s, t):
        # Check if mapping exists and is consistent
        if (a in hash_m and hash_m[a] != b) or (b in hash_m2 and hash_m2[b] != a):
            return False
        hash_m[a] = b
        hash_m2[b] = a

    return True