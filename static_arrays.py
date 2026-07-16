# Static Arrays

# Static arrays have a fixed capacity.
# Accessing an index is fast because each index maps directly to a memory address.


# Initialize an array
my_array = [1, 3, 5, 7, 9, 11]


# Reading from an array
# Time Complexity: O(1)
# Space Complexity: O(1)
print("Read index 3:", my_array[3])


# Traversing an array with a for loop
# Time Complexity: O(n)
# Space Complexity: O(1)
print("Traverse with for loop:")
for i in range(len(my_array)):
    print(my_array[i])


# Traversing an array with a while loop
# Time Complexity: O(n)
# Space Complexity: O(1)
print("Traverse with while loop:")
i = 0
while i < len(my_array):
    print(my_array[i])
    i += 1


def remove_end(arr, length):
    # Remove from the end
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    if length > 0:
        arr[length - 1] = 0


print("Remove from the end:")
print("before:", my_array)
remove_end(my_array, len(my_array))
print("after:", my_array)


def remove_middle(arr, i, length):
    # Remove from the middle by shifting elements left
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]


print("Remove from the middle:")
print("before:", my_array)
remove_middle(my_array, 3, len(my_array))
print("after:", my_array)


def insert_end(arr, n, length, capacity):
    # Insert at the end
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    if length < capacity:
        arr[length] = n


print("Insert at the end:")
print("before:", my_array)
insert_end(my_array, 100, 4, 6)
print("after:", my_array)


def insert_middle(arr, i, n, length):
    # Insert in the middle by shifting elements right
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    arr[i] = n


print("Insert in the middle:")
print("before:", my_array)
insert_middle(my_array, 1, 1000, 5)
print("after:", my_array)


# Static Array Complexity Summary
# Read: O(1)
# Search: O(n)
# Insert at end: O(1)
# Remove from end: O(1)
# Insert in middle: O(n)
# Remove from middle: O(n)
