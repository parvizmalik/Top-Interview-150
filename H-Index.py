

def h_index(citations):
    citations.sort(reverse=True)
    h = 0
    while h < len(citations) and citations[h] > h:
        h += 1
    return h




def h_index(citations):
    n = len(citations)
    # Initialize buckets
    buckets = [0] * (n + 1)

    # Fill buckets
    for citation in citations:
        # If citation count is higher than n, put it in the last bucket
        if citation >= n:
            buckets[n] += 1
        else:
            buckets[citation] += 1

    total = 0
    # Iterate from the end of buckets to find the h-index
    for i in range(n, -1, -1):
        total += buckets[i]
        if total >= i:
            return i
    return 0


# Example usage
citations = [3, 0, 6, 1, 5]
print(h_index(citations))  # Output: 3
