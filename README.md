# Algorithms

This repository is for tracking data structures, algorithms, notes, and LeetCode solutions as I work through them.

## Table of Contents

- [Algorithms and Data Structures for Beginners](#algorithms-and-data-structures-for-beginners)
  - [Arrays](#arrays)
    - [Static Arrays](#static-arrays)
    - [Dynamic Arrays](#dynamic-arrays)
  - [Stacks](#stacks)
- [Patterns](#patterns)
  - [Two Pointers](#two-pointers)
  - [Simulation](#simulation)
  - [Counting](#counting)
    - [Inclusion-Exclusion](#inclusion-exclusion)
  - [Prefix Sum](#prefix-sum)
  - [Math](#math)
    - [Euclidean Algorithm](#euclidean-algorithm)
- [Completed Problems](#completed-problems)
- [Daily Problems](#daily-problems)

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

Notes: [static_arrays.py](notes/static_arrays.py)

#### Suggested Problems

| Completed | Difficulty | Pattern | Problem | Solution | Notes |
| :---: | --- | --- | --- | --- | --- |
| ✔️ | 🟢 Easy | Two Pointers | [27. Remove Element](https://leetcode.com/problems/remove-element/) | [27_remove_element.py](problems/27_remove_element.py) | In-place array overwrite, two pointers |
| ✔️ | 🟢 Easy | Sliding Window | [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | [485_max_consecutive_ones.py](problems/485_max_consecutive_ones.py) | Linear scan, counting streaks |
| ✔️ | 🟢 Easy | Suffix Maximum | [1299. Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | [1299_replace_elements.py](problems/1299_replace_elements.py) | Brute force, suffix maximum |

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

Notes: [dynamic_arrays.py](notes/dynamic_arrays.py)

#### Suggested Problems

| Completed | Difficulty | Pattern | Problem | Solution | Notes |
| :---: | --- | --- | --- | --- | --- |
| ✔️ | 🟢 Easy | Array Construction | [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | [1929_concatenation_of_array.py](problems/1929_concatenation_of_array.py) | Return the array repeated twice |

## Stacks

A stack is a linear data structure where elements are added and removed from the same end, called the top of the stack. It follows `LIFO`: last in, first out.

Stacks can be implemented with an array or linked list. In Python, a list works well because `append`, `pop`, and reading the last element are all efficient end-of-array operations.

If a stack has a fixed capacity, pushing onto a full stack causes stack overflow. Popping from an empty stack causes stack underflow. In Python, lists grow dynamically, but it is still good practice to check whether a stack is empty before popping or peeking.

Common stack operations:

| Operation | Time Complexity | Notes |
| --- | --- | --- |
| Push | O(1) | Add to the top of the stack |
| Pop | O(1) | Remove from the top; check for empty stack first |
| Peek / Top | O(1) | Read the top without removing it |
| Is Empty | O(1) | Check whether the stack has no elements |
| Size | O(1) | Track or return the number of elements |

Stacks are useful when you need to process items in reverse order, undo recent work, match pairs like parentheses, evaluate expressions, or keep track of nested state.

Look for:

- Reverse order processing, where the last item added should be handled first.
- Nested structures, such as parentheses, brackets, function calls, or expression parsing.
- State tracking, undo/redo behavior, browser history, or backtracking recent actions.
- Problems that only need access to the most recent item, not random access or searching.

Notes: [stacks.py](notes/stacks.py)

#### Suggested Problems

| Completed | Difficulty | Pattern | Problem | Solution | Notes |
| :---: | --- | --- | --- | --- | --- |
| ⬜ | 🟢 Easy | Stack | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [20_valid_parentheses.py](problems/20_valid_parentheses.py) | Match opening and closing brackets |
| ⬜ | 🟢 Easy | Stack | [682. Baseball Game](https://leetcode.com/problems/baseball-game/) | [682_baseball_game.py](problems/682_baseball_game.py) | Track previous scores |
| ⬜ | 🟡 Medium | Stack | [155. Min Stack](https://leetcode.com/problems/min-stack/) | [155_min_stack.py](problems/155_min_stack.py) | Track minimum while supporting stack operations |

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

### Simulation

Use simulation when the problem gives a direct process to follow step by step. The solution usually keeps track of some state, applies each rule in order, and returns the final result after the process is complete.

Simulation problems are often not about finding a hidden trick. The main job is to model the instructions cleanly, update state carefully, and avoid unnecessary extra work.

Look for:

- A problem statement that describes an exact sequence of operations.
- State that changes over time, such as a running maximum, score, position, stack, queue, or list.
- Instructions like build, process, sort, pair, remove, repeat, or ignore.
- A result that comes from following the rules directly.

### Counting

Use counting when the direct approach would build too many values, but the problem only needs to know how many times each value or category appears.

For 3312, building every GCD pair is too slow because there are `O(n^2)` pairs. Instead, count how many pairs have each possible GCD value.

#### Inclusion-Exclusion

Inclusion-exclusion removes over-counting. For GCD problems, if we count all pairs where both numbers are divisible by `g`, that includes pairs whose exact GCD is `g`, but also pairs whose exact GCD is `2g`, `3g`, and other multiples.

To fix this, calculate exact GCD counts from large to small. When processing `g`, subtract the already-known counts for larger multiples of `g`.

### Prefix Sum

Use prefix sums when you need fast cumulative counts or range totals. After counting how many pairs have each GCD value, a prefix sum lets us know how many sorted GCD pairs are `<= g`.

For query problems, prefix sums often pair with binary search: find the first prefix count that passes the query index.

### Math

#### Euclidean Algorithm

Use the Euclidean algorithm to find the greatest common divisor, or `gcd`, of two numbers. The key idea is that `gcd(a, b) == gcd(b, a % b)`, and the recursion stops when the second number becomes `0`.

```python
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
```

For 3658, the first `n` odd numbers sum to `n * n`, and the first `n` even numbers sum to `n * (n + 1)`. Since `n` and `n + 1` are consecutive, their GCD is `1`, so the answer simplifies to `n`.

## Completed Problems

| # | Completed | Difficulty | Pattern | Problem | Topic | Solution | Completed On |
| --- | :---: | --- | --- | --- | --- | --- | --- |
| 27 | ✔️ | 🟢 Easy | Two Pointers | [Remove Element](https://leetcode.com/problems/remove-element/) | Static Arrays | [27_remove_element.py](problems/27_remove_element.py) | 2026-07-16 |
| 485 | ✔️ | 🟢 Easy | Sliding Window | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Static Arrays | [485_max_consecutive_ones.py](problems/485_max_consecutive_ones.py) | 2026-07-16 |
| 1299 | ✔️ | 🟢 Easy | Suffix Maximum | [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | Static Arrays | [1299_replace_elements.py](problems/1299_replace_elements.py) | 2026-07-16 |
| 1929 | ✔️ | 🟢 Easy | Array Construction | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Dynamic Arrays | [1929_concatenation_of_array.py](problems/1929_concatenation_of_array.py) | 2026-07-16 |
| 3658 | ✔️ | 🟢 Easy | Math / Euclidean Algorithm | [GCD of Odd and Even Sums](https://leetcode.com/problems/gcd-of-odd-and-even-sums/) | Math | [3658_gcd_of_odd_and_even_sums.py](problems/3658_gcd_of_odd_and_even_sums.py) | 2026-07-17 |
| 3867 | ✔️ | 🟡 Medium | Simulation / Euclidean Algorithm | [Sum of GCD of Formed Pairs](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/) | Math / Sorting | [3867_sum_of_gcd_of_formed_pairs.py](problems/3867_sum_of_gcd_of_formed_pairs.py) | 2026-07-17 |
| 3312 | ❌ | 🔴 Hard | Counting / Inclusion-Exclusion / Prefix Sum | [Sorted GCD Pair Queries](https://leetcode.com/problems/sorted-gcd-pair-queries/) | Math / Number Theory | [3312_sorted_gcd_pair_queries.py](daily-problems/3312_sorted_gcd_pair_queries.py) | 2026-07-17 |

## Daily Problems

| Date | # | Completed | Difficulty | Pattern | Problem | Solution |
| --- | --- | :---: | --- | --- | --- | --- |
| 2026-07-17 | 3312 | ❌ | 🔴 Hard | Counting / Inclusion-Exclusion / Prefix Sum | [Sorted GCD Pair Queries](https://leetcode.com/problems/sorted-gcd-pair-queries/) | [3312_sorted_gcd_pair_queries.py](daily-problems/3312_sorted_gcd_pair_queries.py) |
