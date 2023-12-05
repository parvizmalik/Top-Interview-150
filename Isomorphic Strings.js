function isIsomorphic(s, t) {
    const hashM = {};
    const hashM2 = {};

    for (let i = 0; i < s.length; i++) {
        const a = s[i];
        const b = t[i];

        // Check if the mapping exists and is consistent
        if ((hashM[a] !== undefined && hashM[a] !== b) || (hashM2[b] !== undefined && hashM2[b] !== a)) {
            return false;
        }

        // Update the mappings
        hashM[a] = b;
        hashM2[b] = a;
    }

    return true;
}
