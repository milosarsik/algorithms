# Algorithms

This repository is for tracking data structures, algorithms, notes, and LeetCode solutions as I work through them.

## Table of Contents

- [Algorithms and Data Structures for Beginners](#algorithms-and-data-structures-for-beginners)
  - [Arrays](#arrays)
    - [Static Arrays](#static-arrays)
    - [Dynamic Arrays](#dynamic-arrays)
- [Patterns](#patterns)
  - [Two Pointers](#two-pointers)
- [Completed Problems](#completed-problems)

## Algorithms and Data Structures for Beginners

## Arrays

Arrays store values in contiguous memory. Reading from an index is efficient because the index maps directly to a memory address.

### Static Arrays

Static arrays have a fixed capacity. Python lists are dynamic arrays, but the same concepts are useful when learning how array operations work.

| Operation | Time Complexity | Notes |
| --- | --- | --- |
| Read or write i-th element | O(1) | Direct index access |
| Search for value | O(n) | May need to scan every element |
| Insert at end | O(1) | Only if there is available capacity |
| Remove from end | O(1) | No shifting needed |
| Insert in middle | O(n) | Elements must shift right |
| Remove from middle | O(n) | Elements must shift left |

Notes: [static_arrays.py](static_arrays.py)

#### Suggested Problems

| Completed | Difficulty | Pattern | Problem | Solution | Notes |
| :---: | --- | --- | --- | --- | --- |
| ✔️ | 🟢 Easy | Two Pointers | [27. Remove Element](https://leetcode.com/problems/remove-element/) | [27_remove_element.py](27_remove_element.py) | In-place array overwrite, two pointers |
| ✔️ | 🟢 Easy | Sliding Window | [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | [485_max_consecutive_ones.py](485_max_consecutive_ones.py) | Linear scan, counting streaks |
| ✔️ | 🟢 Easy | Suffix Maximum | [1299. Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | [1299_replace_elements.py](1299_replace_elements.py) | Brute force, suffix maximum |

### Dynamic Arrays

Dynamic arrays grow as elements are added. Python lists are dynamic arrays, so unlike static arrays, you do not need to choose the final size up front.

When a dynamic array runs out of capacity, it creates a new array with more space, usually double the old capacity, copies the existing elements over, and then inserts the new value. That resize step is `O(n)`, but it does not happen on every insertion. Because capacity doubles, adding to the end is `O(1)` amortized over many insertions.

Inserting or removing from the middle still requires shifting elements, so those operations remain `O(n)`.

| Operation | Time Complexity | Notes |
| --- | --- | --- |
| Read or write i-th element | O(1) | Direct index access |
| Search for value | O(n) | May need to scan every element |
| Insert at end | O(1) amortized | Resize is O(n), but not every insert resizes |
| Remove from end | O(1) | No shifting needed |
| Resize | O(n) | Copy elements into a larger array |
| Insert in middle | O(n) | Elements must shift right |
| Remove from middle | O(n) | Elements must shift left |

Notes: [dynamic_arrays.py](dynamic_arrays.py)

#### Suggested Problems

| Completed | Difficulty | Pattern | Problem | Solution | Notes |
| :---: | --- | --- | --- | --- | --- |
| ✔️ | 🟢 Easy | Array Construction | [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | [1929_concatenation_of_array.py](1929_concatenation_of_array.py) | Return the array repeated twice |

## Patterns

### Two Pointers

Use two pointers when a problem asks you to process elements from two positions in a linear structure like an array, string, or linked list. The pointers may start at opposite ends, at different positions in the same structure, or across two related structures.

This pattern is useful when pointer movement can be decided from the current values. For example, in a sorted array pair-sum problem, move the right pointer left when the sum is too large and move the left pointer right when the sum is too small. For palindrome checks or array reversal, move both pointers toward the middle.

Two pointers often replaces nested loops with a single pass, improving time complexity from `O(n^2)` to `O(n)` while usually keeping space complexity at `O(1)`.

Look for:

- A linear data structure.
- A need to compare, swap, remove, or combine values from two positions.
- A sorted input, palindrome-style symmetry, in-place compaction, or pair/triplet search.
- Pointer movement rules based on conditions in the problem.

## Completed Problems

| # | Completed | Difficulty | Pattern | Problem | Topic | Solution | Completed On |
| --- | :---: | --- | --- | --- | --- | --- | --- |
| 27 | ✔️ | 🟢 Easy | Two Pointers | [Remove Element](https://leetcode.com/problems/remove-element/) | Static Arrays | [27_remove_element.py](27_remove_element.py) | 2026-07-16 |
| 485 | ✔️ | 🟢 Easy | Sliding Window | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Static Arrays | [485_max_consecutive_ones.py](485_max_consecutive_ones.py) | 2026-07-16 |
| 1299 | ✔️ | 🟢 Easy | Suffix Maximum | [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | Static Arrays | [1299_replace_elements.py](1299_replace_elements.py) | 2026-07-16 |
| 1929 | ✔️ | 🟢 Easy | Array Construction | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Dynamic Arrays | [1929_concatenation_of_array.py](1929_concatenation_of_array.py) | 2026-07-16 |
