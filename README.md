# Algorithms

This repository is for tracking data structures, algorithms, notes, and LeetCode solutions as I work through them.

## Table of Contents

- [Algorithms and Data Structures for Beginners](#algorithms-and-data-structures-for-beginners)
  - [Arrays](#arrays)
    - [Static Arrays](#static-arrays)
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

| Completed | Problem | Solution | Notes |
| --- | --- | --- | --- |
| Done | [27. Remove Element](https://leetcode.com/problems/remove-element/) | [27_remove_element.py](27_remove_element.py) | In-place array overwrite, two pointers |
| Done | [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | [485_max_consecutive_ones.py](485_max_consecutive_ones.py) | Linear scan, counting streaks |
| Done | [1299. Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | [1299_replace_elements.py](1299_replace_elements.py) | Brute force, suffix maximum |

## Completed Problems

| # | Problem | Topic | Solution | Status |
| --- | --- | --- | --- | --- |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | Arrays / Two Pointers | [27_remove_element.py](27_remove_element.py) | Done |
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Arrays | [485_max_consecutive_ones.py](485_max_consecutive_ones.py) | Done |
| 1299 | [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | Arrays | [1299_replace_elements.py](1299_replace_elements.py) | Done |
