def reverseWords(s: str) -> str:
    return ' '.join(reversed(s.split()))


# Example usage:
example = "the sky is blue"
output = reverseWords(example)



# SOLUTION 2 //////////////////////////////////////////////

def reverseWords(s: str) -> str:
    return ' '.join(s.split()[::-1])


# Example usage:
example = "the sky is blue"
output = reverseWords(example)

# SOLUTION 3     //////////////////////////////////////////////


def reverseWords(s: str) -> str:
    words = []
    length = len(s)
    i = 0

    while i < length:
        if s[i] != ' ':
            start = i
            while i < length and s[i] != ' ':
                i += 1
            words.append(s[start:i])
        i += 1

    return ' '.join(reversed(words))


# Example usage:
example = "the sky is blue"
output = reverseWords(example)
