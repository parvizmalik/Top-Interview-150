function canCompleteCircuit(gas, cost) {
  let totalGas = 0,
    currentGas = 0,
    startStation = 0;

  for (let i = 0; i < gas.length; i++) {
    let netGas = gas[i] - cost[i];
    totalGas += netGas;
    currentGas += netGas;

    if (currentGas < 0) {
      startStation = i + 1;
      currentGas = 0;
    }
  }

  return totalGas >= 0 ? startStation : -1;
}

// Example usage
console.log(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])); // Output: 3
console.log(canCompleteCircuit([2, 3, 4], [3, 4, 3])); // Output: -1
