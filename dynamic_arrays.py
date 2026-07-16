# Dynamic Arrays


class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        # Read i-th element
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Write i-th element
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Insert at the end
        # Time Complexity: O(1) amortized
        # Space Complexity: O(1)
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # Remove from the end
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        if self.length > 0:
            self.length -= 1

        return self.arr[self.length]

    def resize(self) -> None:
        # Double capacity and copy elements into the new array
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        self.capacity = 2 * self.capacity
        tmp = [0] * self.capacity

        for i in range(self.length):
            tmp[i] = self.arr[i]

        self.arr = tmp

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity


# Dynamic Array Complexity Summary
# Read or write i-th element: O(1)
# Search: O(n)
# Insert at end: O(1) amortized
# Remove from end: O(1)
# Resize: O(n)
# Insert in middle: O(n)
# Remove from middle: O(n)
