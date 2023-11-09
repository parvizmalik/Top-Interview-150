function hIndex(citations) {
  const n = citations.length;
  // Initialize buckets
  const buckets = new Array(n + 1).fill(0);

  // Fill buckets
  citations.forEach((citation) => {
    // If citation count is higher than n, put it in the last bucket
    buckets[Math.min(n, citation)] += 1;
  });

  let total = 0;
  // Iterate from the end of buckets to find the h-index
  for (let i = n; i >= 0; i--) {
    total += buckets[i];
    if (total >= i) {
      return i;
    }
  }
  return 0;
}

// Example usage:
const citations = [3, 0, 6, 1, 5];
console.log(hIndex(citations)); // Output should be 3







function hIndex(citations) {
  citations.sort((a, b) => b - a); // Sort in descending order
  let h = 0;
  while (h < citations.length && citations[h] > h) {
    h++;
  }
  return h;
}

// Example usage:
const citations = [3, 0, 6, 1, 5];
console.log(hIndex(citations)); // Output should be 3
