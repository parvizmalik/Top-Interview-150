class RandomizedSet {
    constructor() {
        this.list = [];
        this.hashMap = new Map();
    }

    insert(val) {
        if (this.hashMap.has(val)) {
            return false;
        }
        this.hashMap.set(val, this.list.length);
        this.list.push(val);
        return true;
    }

    remove(val) {
        if (!this.hashMap.has(val)) {
            return false;
        }
        const index = this.hashMap.get(val);
        const lastElement = this.list[this.list.length - 1];

        // Swap the last element with the element to remove
        this.list[index] = lastElement;
        this.hashMap.set(lastElement, index);

        // Remove the last element
        this.list.pop();
        this.hashMap.delete(val);

        return true;
    }

    getRandom() {
        const randomIndex = Math.floor(Math.random() * this.list.length);
        return this.list[randomIndex];
    }
}

// Example usage
const randomizedSet = new RandomizedSet();
console.log(randomizedSet.insert(1)); // Outputs: true
console.log(randomizedSet.remove(2)); // Outputs: false
console.log(randomizedSet.insert(2)); // Outputs: true
console.log(randomizedSet.getRandom()); // Outputs: 1 or 2 randomly
console.log(randomizedSet.remove(1)); // Outputs: true
console.log(randomizedSet.insert(2)); // Outputs: false
console.log(randomizedSet.getRandom()); // Outputs: 2
