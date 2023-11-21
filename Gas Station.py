def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total_gas, current_gas, start_station = 0, 0, 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            start_station = i + 1
            current_gas = 0

    return start_station if total_gas >= 0 else -1

# Example usage
gas1 = [1, 2, 3, 4, 5]
cost1 = [3, 4, 5, 1, 2]
print(can_complete_circuit(gas1, cost1))  # Output: 3

gas2 = [2, 3, 4]
cost2 = [3, 4, 3]
print(can_complete_circuit(gas2, cost2))  # Output: -1
