def replace_elements_brute_force(arr):
    # Brute force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    largest = -1
    for i in range(len(arr)):
        largest = -1
        for k in range(i + 1, len(arr)):
            largest = max(largest, arr[k])
        arr[i] = largest

    return arr


def replace_elements_suffix_max(arr):
    # Suffix max
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    res = [0] * len(arr)
    right_max = -1

    for i in range(len(arr) - 1, -1, -1):
        res[i] = right_max
        right_max = max(arr[i], right_max)

    return res


def replace_elements_in_place(arr):
    # In-place suffix max
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    largest = -1

    for i in range(len(arr) - 1, -1, -1):
        arr[i], largest = largest, max(largest, arr[i])

    return arr


arr = [17, 18, 5, 4, 6, 1]

print("brute force:", replace_elements_brute_force(arr.copy()))
print("suffix max:", replace_elements_suffix_max(arr.copy()))
print("in place:", replace_elements_in_place(arr.copy()))

arr = [400]

print("brute force:", replace_elements_brute_force(arr.copy()))
print("suffix max:", replace_elements_suffix_max(arr.copy()))
print("in place:", replace_elements_in_place(arr.copy()))
