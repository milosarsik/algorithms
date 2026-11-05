# Insertion Sort
# NeetCode lesson and self-written practice, 2026-11-05.

# Algorithm in English:
# 1. Treat the first element as an already-sorted prefix of length one.
# 2. Start i at 1 and insert each next element into that sorted prefix.
# 3. Set j = i - 1. The element being inserted is currently at j + 1.
# 4. While j is valid and the adjacent pair is out of order, swap them.
# 5. Decrease j to follow the inserted element as it moves left.
# 6. Stop at the beginning or when the left neighbor is <= the inserted value.
# After each outer iteration, arr[0] through arr[i] are sorted.
# This describes a prefix; the implementation does not copy or slice it.

# Stability: strict < prevents equal elements from crossing each other.
# With labels showing identity: [7a, 3, 7b] becomes [3, 7a, 7b].
# Using <= would swap equal values and lose this stability guarantee.
# Values must support a consistent comparison; integers are not required.

# Time Complexity (constant-time comparisons):
# Best: O(n), already sorted; the inner loop body never runs.
# Average: O(n^2) for randomly ordered input.
# Worst: O(n^2), reverse-sorted distinct values. Outer iteration i needs i
# swaps, so the total is 1 + 2 + ... + (n - 1) = n * (n - 1) / 2.
# Space Complexity: O(1) extra space; swaps modify the original list.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1

        # Check the boundary first: Python's arr[-1] is a valid index, but it
        # refers to the last element, not a neighbor before the array start.
        while j >= 0 and arr[j + 1] < arr[j]:
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp
            j -= 1

    return arr


arr = [5, 3, 4, 2, 1]
print("before:", arr)
arr = insertion_sort(arr)
print("after:", arr)  # [1, 2, 3, 4, 5]

print("already sorted:", insertion_sort([1, 2, 3]))  # [1, 2, 3]
print("reverse sorted:", insertion_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print("duplicates:", insertion_sort([7, 3, 7]))  # [3, 7, 7]
print("negative values:", insertion_sort([0, -2, 3, -1]))  # [-2, -1, 0, 3]
print("empty:", insertion_sort([]))  # []
print("single value:", insertion_sort([4]))  # [4]

# Review cues:
# - i selects the next insertion; j follows that value left through swaps.
# - The element moves away from its original index i as swaps happen.
# - Return arr returns the same list, not a newly allocated sorted copy.
# - Useful for small or nearly sorted inputs; large disordered inputs can
#   require quadratic work. This version is iterative, not recursive.
