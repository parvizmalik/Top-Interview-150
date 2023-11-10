import random

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hash_map = {}

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        index = self.hash_map[val]
        last_element = self.list[-1]
        
        self.list[index] = last_element
        self.hash_map[last_element] = index
        
        self.list.pop()
        del self.hash_map[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)

# Example usage
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1)) # True
print(randomizedSet.remove(2)) # False
print(randomizedSet.insert(2)) # True
print(randomizedSet.getRandom()) # 1 or 2
print(randomizedSet.remove(1)) # True
print(randomizedSet.insert(2)) # False
print(randomizedSet.getRandom()) # 2





########################################################################## SOLUTION 2


import random

class RandomizedSet:
    def __init__(self):
        self.num_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        self.num_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        last_val = self.nums[-1]
        idx_to_swap = self.num_to_index[val]
        self.nums[idx_to_swap], self.num_to_index[last_val] = last_val, idx_to_swap
        self.nums.pop()
        del self.num_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Example usage
randomized_set = RandomizedSet()
print(randomized_set.insert(1))  # Outputs: True
print(randomized_set.remove(2))  # Outputs: False
print(randomized_set.insert(2))  # Outputs: True
print(randomized_set.getRandom()) # Outputs: 1 or 2 randomly

