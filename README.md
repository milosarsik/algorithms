# Algorithms

This repository is for tracking data structures, algorithms, notes, and LeetCode solutions as I work through them.

## DSA Plan

Use the resources hierarchically:

| Resource | Role |
| --- | --- |
| NeetCode | Syllabus and problem selection |
| LeetCode | Implementation environment |
| Grokking Patterns | Explanation when a pattern is unclear |
| EPI Python | Selected deeper explanations and additional drills |

Do not study all four independently.

### Eight-Week Sequence

1. Arrays and hashing
2. Two pointers and sliding window
3. Stacks, queues, and binary search
4. Linked lists and trees
5. BFS, DFS, and heaps
6. Graphs, intervals, topological sort, union-find
7. Backtracking and basic dynamic programming
8. Mixed timed assessments

### Weekly Targets

- 6-8 new problems
- 4 repeated problems
- One 90-minute timed assessment
- One mistake-review session

### Problem Protocol

For each problem:

1. Explain the brute-force approach.
2. Identify the likely pattern.
3. Attempt independently for approximately 25-30 minutes.
4. Take a small hint if completely blocked.
5. Study the solution only after a real attempt.
6. Close it and reproduce it without looking.
7. Repeat it after approximately 3 days and again after 1-2 weeks.

For spaced repetition, use this cadence:

- Failed or low-confidence problem: review after 1 day, then 3 days, 7 days, 14 days, and 30 days.
- Solved but shaky problem: review after 3 days, then 7 days, 14 days, and 30 days.
- Easy/high-confidence problem: review after 7-14 days, then 30 days.

### Review Protocol

For DSA reviews:

1. Blank attempt first.

Open a blank editor or notebook. Do not open the saved solution yet. Write:

- Problem goal
- Input/output
- Pattern
- Brute-force idea
- Optimized idea
- Time/space complexity

2. Try code from memory for 10-15 minutes.

If stuck, do not immediately read the full solution. First write the missing step in English:

- "I need to save the next node before rewiring."
- "I need a dummy node so first insertion is not special."
- "I need DFS from the suspicious method."

3. Use tiny hints.

Look only at the README pattern note or attempt notes first. Then check the algorithm-in-English comments. Only open the full code if still stuck.

4. Close the solution and reproduce.

After checking, close the solution and rewrite the whole solution once without looking. This is the part that actually locks it in.

5. Record the failure mode.

Write one sentence:

- "Forgot pointer update order."
- "Forgot to clear forward history."
- "Recognized linked list but forgot dummy node."
- "Could not identify DFS reachability."

Record:

- Pattern
- Recognition failure
- Reasoning failure
- Python/API mistake
- Time complexity
- Cue you should recognize next time
- Repeat date

## Table of Contents

- [DSA Plan](#dsa-plan)
  - [Eight-Week Sequence](#eight-week-sequence)
  - [Weekly Targets](#weekly-targets)
  - [Problem Protocol](#problem-protocol)
  - [Review Protocol](#review-protocol)
- [Legend](#legend)
- [Algorithms and Data Structures for Beginners](#algorithms-and-data-structures-for-beginners)
  - [Arrays](#arrays)
    - [Static Arrays](#static-arrays)
    - [Dynamic Arrays](#dynamic-arrays)
  - [Stacks](#stacks)
  - [Linked Lists](#linked-lists)
    - [Singly Linked Lists](#singly-linked-lists)
    - [Doubly Linked Lists](#doubly-linked-lists)
- [Patterns](#patterns)
  - [Two Pointers](#two-pointers)
  - [In-Place Linked List Manipulation](#in-place-linked-list-manipulation)
  - [Linked List Merge](#linked-list-merge)
  - [Simulation](#simulation)
  - [Counting](#counting)
    - [Inclusion-Exclusion](#inclusion-exclusion)
  - [Prefix Sum](#prefix-sum)
  - [String Building](#string-building)
  - [Enumeration](#enumeration)
  - [Graph Traversal](#graph-traversal)
  - [Math](#math)
    - [Euclidean Algorithm](#euclidean-algorithm)
- [Completed Problems](#completed-problems)
- [Daily Problems](#daily-problems)
- [Programming Skills Study Plan](#programming-skills-study-plan)
  - [Basic Implementation](#basic-implementation)
- [Tricks](#tricks)

## Legend

| Symbol | Meaning |
| :---: | --- |
| ✔️ | Solved independently |
| 🟡 | Solved with hints or partial help |
| ❌ | Reviewed solution / did not solve |
| ⬜ | Not started |

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
| ✔️ | 🟢 Easy | Stack | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [20_valid_parentheses.py](problems/20_valid_parentheses.py) | Match opening and closing brackets |
| ✔️ | 🟢 Easy | Stack | [682. Baseball Game](https://leetcode.com/problems/baseball-game/) | [682_baseball_game.py](problems/682_baseball_game.py) | Track previous scores |
| ✔️ | 🟡 Medium | Stack / Design | [155. Min Stack](https://leetcode.com/problems/min-stack/) | [155_min_stack.py](problems/155_min_stack.py) | Track minimum while supporting stack operations |

## Linked Lists

Linked lists store values in nodes. Each node has a value and a pointer to the next node. Unlike arrays, nodes do not need to be next to each other in memory, so linked lists are good for pointer-based insertions and deletions when you already have the relevant node reference.

The tradeoff is that linked lists do not support direct index access. To find a value or reach a position, you usually start at the head and follow `next` pointers one node at a time.

### Singly Linked Lists

A singly linked list moves in one direction from `head` to `tail`. The final node points to `None`. If a node points back to an earlier node, the list has a cycle and normal traversal can loop forever.

| Operation | Time Complexity | Notes |
| --- | --- | --- |
| Access by index | O(n) | Must traverse from the head |
| Search | O(n) | May need to inspect every node |
| Insert after known node | O(1) | Rewire one or two pointers |
| Delete after known node | O(1) | Skip over the removed node |
| Append with tail pointer | O(1) | Link the new node and update tail |
| Append without tail pointer | O(n) | Must traverse to the end first |

For in-place linked list problems, the key move is usually pointer rewiring. For example, reversing a list uses `previous`, `current`, and `next_node` so you can reverse each `next` pointer without losing the rest of the list.

The notes file also includes a simple `LinkedList` class with a dummy head node and tail pointer. The dummy head makes removing index `0` behave like removing any other index, and the tail pointer makes appending to the end `O(1)`.

Notes: [singly_linked_lists.py](notes/singly_linked_lists.py)

#### Suggested Problems

| Completed | Difficulty | Pattern | Problem | Solution | Notes |
| :---: | --- | --- | --- | --- | --- |
| 🟡 | 🟢 Easy | In-Place Linked List Manipulation | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [206_reverse_linked_list.py](problems/206_reverse_linked_list.py) | Reverse pointers with previous/current/next |
| ✔️ | 🟢 Easy | Linked List Merge / Two Pointers | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | [21_merge_two_sorted_lists.py](problems/21_merge_two_sorted_lists.py) | Build merged order by relinking nodes |

### Doubly Linked Lists

A doubly linked list is a linked list where each node points both forward and backward with `next` and `prev`. This makes it possible to traverse in both directions and makes end operations cleaner when the list keeps a tail pointer.

You do not strictly need dummy nodes, but dummy `head` and `tail` nodes are worth using in many implementation problems. They remove awkward edge cases because every real node is always between two nodes, even when the list is empty or has one value.

| Operation | Time Complexity | Notes |
| --- | --- | --- |
| Access by index | O(n) | Must traverse from the head or tail |
| Search | O(n) | May need to inspect every node |
| Insert at front | O(1) | Rewire dummy head, first node, and new node |
| Insert at end | O(1) | Rewire dummy tail, last node, and new node |
| Remove from front | O(1) | Check for empty list first |
| Remove from end | O(1) | Check for empty list first |
| Insert/delete after known node | O(1) | Assuming you already have the node reference |

Common mistakes are forgetting to update both directions of a link, losing the old first or last node before rewiring, and not handling an empty list before removal.

Notes: [doubly_linked_lists.py](notes/doubly_linked_lists.py)

#### Suggested Problems

| Completed | Difficulty | Pattern | Problem | Solution | Notes |
| :---: | --- | --- | --- | --- | --- |
| ⬜ | 🟡 Medium | Doubly Linked List / Design | [707. Design Linked List](https://leetcode.com/problems/design-linked-list/) | - | Implement indexed get, insert, and delete operations |
| ⬜ | 🟡 Medium | Doubly Linked List / Design | [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/) | - | Move backward and forward through history state |

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

### In-Place Linked List Manipulation

Use in-place linked list manipulation when the input is a linked list and the task asks you to change node order or structure without creating a new list. Instead of copying nodes, rewire existing `next` pointers.

The classic reversal pattern tracks three nodes:

```python
previous = None
current = head

while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
```

Look for:

- A linked list input.
- Requirements like reverse, rotate, reorder, remove, swap, partition, or merge.
- A need to modify links rather than only read values.
- Space constraints asking for `O(1)` extra memory.

### Linked List Merge

Use linked list merge when two sorted linked lists need to become one sorted list. Keep a `current` pointer at the tail of the merged list, repeatedly attach the smaller current node, and advance only the list that provided that node.

A dummy node keeps the code simple because every append looks the same, including the first real node. It also means empty lists are handled naturally: after the main loop, attach whichever list remains with `current.next = list1 if list1 else list2`.

Look for:

- Two sorted linked lists.
- A need to preserve sorted order.
- A result list built by relinking existing nodes.
- Edge cases where either input list may be empty.

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

### String Building

Use string building when a problem asks you to construct a new string step by step. In Python, strings are immutable, so it is usually cleaner and more efficient to append characters to a list and call `"".join(...)` at the end instead of repeatedly concatenating strings in a loop.

Look for:

- A result string that is built one character or chunk at a time.
- Alternating, merging, filtering, reversing, or formatting characters.
- Problems where the output size is proportional to the input size.

### Enumeration

Use enumeration when the search space is small enough to check candidates directly. Start from the first possible answer, test each candidate, and return the first one that satisfies the condition.

Look for:

- Small constraints.
- A request for the smallest or first valid value.
- Hints that only a bounded number of candidates need checking.
- A simple predicate that can be tested for each candidate.

### Graph Traversal

Use graph traversal when values are connected by relationships and the answer depends on what can be reached from a starting point. Build an adjacency list, then use DFS or BFS to visit reachable nodes.

DFS is often a good fit when you need to mark everything connected to one source, such as all methods reachable from a buggy method. For directed graphs, be careful with edge direction: if `a` invokes `b`, the traversal edge is `a -> b`.

Look for:

- Nodes and edges, dependencies, calls, prerequisites, routes, or relationships.
- Language like reachable, connected, direct or indirect, invokes, depends on, or visits.
- A starting node where everything reachable from it must be marked.
- A need to check whether an outside node points into a marked group.

### Math

#### Euclidean Algorithm

Use the Euclidean algorithm to find the greatest common divisor, or `gcd`, of two numbers. The key idea is that `gcd(a, b) == gcd(b, a % b)`, and the recursion stops when the second number becomes `0`.

```python
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
```

Python also has this built in:

```python
import math

math.gcd(a, b)
```

For array problems that ask for the GCD of the smallest and largest values, find `min(nums)` and `max(nums)` first, then run GCD on those two numbers.

For 3658, the first `n` odd numbers sum to `n * n`, and the first `n` even numbers sum to `n * (n + 1)`. Since `n` and `n + 1` are consecutive, their GCD is `1`, so the answer simplifies to `n`.

## Completed Problems

| # | Completed | Difficulty | Pattern | Problem | Topic | Solution | Completed On | Confidence | Next Review | Reviews |
| --- | :---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 27 | ✔️ | 🟢 Easy | Two Pointers | [Remove Element](https://leetcode.com/problems/remove-element/) | Static Arrays | [27_remove_element.py](problems/27_remove_element.py) | 2026-07-16 | - | - | - |
| 485 | ✔️ | 🟢 Easy | Sliding Window | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Static Arrays | [485_max_consecutive_ones.py](problems/485_max_consecutive_ones.py) | 2026-07-16 | - | - | - |
| 1299 | ✔️ | 🟢 Easy | Suffix Maximum | [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | Static Arrays | [1299_replace_elements.py](problems/1299_replace_elements.py) | 2026-07-16 | - | - | - |
| 1929 | ✔️ | 🟢 Easy | Array Construction | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Dynamic Arrays | [1929_concatenation_of_array.py](problems/1929_concatenation_of_array.py) | 2026-07-16 | - | - | - |
| 3658 | ✔️ | 🟢 Easy | Math / Euclidean Algorithm | [GCD of Odd and Even Sums](https://leetcode.com/problems/gcd-of-odd-and-even-sums/) | Math | [3658_gcd_of_odd_and_even_sums.py](problems/3658_gcd_of_odd_and_even_sums.py) | 2026-07-17 | - | - | - |
| 3867 | ✔️ | 🟡 Medium | Simulation / Euclidean Algorithm | [Sum of GCD of Formed Pairs](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/) | Math / Sorting | [3867_sum_of_gcd_of_formed_pairs.py](problems/3867_sum_of_gcd_of_formed_pairs.py) | 2026-07-17 | - | - | - |
| 3312 | ❌ | 🔴 Hard | Counting / Inclusion-Exclusion / Prefix Sum | [Sorted GCD Pair Queries](https://leetcode.com/problems/sorted-gcd-pair-queries/) | Math / Number Theory | [3312_sorted_gcd_pair_queries.py](daily-problems/3312_sorted_gcd_pair_queries.py) | 2026-07-17 | - | - | - |
| 1768 | ✔️ | 🟢 Easy | Two Pointers / String Building | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | String | [1768_merge_strings_alternately.py](study-plan-problems/1768_merge_strings_alternately.py) | 2026-07-17 | - | - | - |
| 20 | ✔️ | 🟢 Easy | Stack | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack / String | [20_valid_parentheses.py](problems/20_valid_parentheses.py) | 2026-07-17 | - | - | - |
| 682 | ✔️ | 🟢 Easy | Stack / Simulation | [Baseball Game](https://leetcode.com/problems/baseball-game/) | Stack | [682_baseball_game.py](problems/682_baseball_game.py) | 2026-07-17 | - | - | - |
| 155 | ✔️ | 🟡 Medium | Stack / Design | [Min Stack](https://leetcode.com/problems/min-stack/) | Stack / Design | [155_min_stack.py](problems/155_min_stack.py) | 2026-07-17 | - | - | - |
| 1979 | ✔️ | 🟢 Easy | Math / Euclidean Algorithm | [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | Array / Math / Number Theory | [1979_find_greatest_common_divisor_of_array.py](daily-problems/1979_find_greatest_common_divisor_of_array.py) | 2026-07-18 | High | - | - |
| 3310 | ❌ | 🟡 Medium | Graph / DFS | [Remove Methods From Project](https://leetcode.com/problems/remove-methods-from-project/) | Graph / DFS / BFS | [3310_remove_methods_from_project.py](daily-problems/3310_remove_methods_from_project.py) | 2026-08-05 | Needs Review | 2026-08-09 | 1 |
| 3345 | ✔️ | 🟢 Easy | Enumeration / Digit Processing | [Smallest Divisible Digit Product I](https://leetcode.com/problems/smallest-divisible-digit-product-i/) | Math / Enumeration | [3345_smallest_divisible_digit_product_i.py](daily-problems/3345_smallest_divisible_digit_product_i.py) | 2026-08-06 | Needs Review | 2026-08-09 | 0 |
| 206 | 🟡 | 🟢 Easy | In-Place Linked List Manipulation | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List / Recursion | [206_reverse_linked_list.py](problems/206_reverse_linked_list.py) | 2026-08-06 | Needs Review | 2026-08-09 | 0 |
| 21 | ✔️ | 🟢 Easy | Linked List Merge / Two Pointers | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked List / Recursion | [21_merge_two_sorted_lists.py](problems/21_merge_two_sorted_lists.py) | 2026-08-07 | Needs Review | 2026-08-10 | 0 |

## Daily Problems

| Date | # | Completed | Difficulty | Pattern | Problem | Solution | Confidence | Next Review | Reviews |
| --- | --- | :---: | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-17 | 3312 | ❌ | 🔴 Hard | Counting / Inclusion-Exclusion / Prefix Sum | [Sorted GCD Pair Queries](https://leetcode.com/problems/sorted-gcd-pair-queries/) | [3312_sorted_gcd_pair_queries.py](daily-problems/3312_sorted_gcd_pair_queries.py) | - | - | - |
| 2026-07-18 | 1979 | ✔️ | 🟢 Easy | Math / Euclidean Algorithm | [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | [1979_find_greatest_common_divisor_of_array.py](daily-problems/1979_find_greatest_common_divisor_of_array.py) | High | - | - |
| 2026-08-05 | 3310 | ❌ | 🟡 Medium | Graph / DFS | [Remove Methods From Project](https://leetcode.com/problems/remove-methods-from-project/) | [3310_remove_methods_from_project.py](daily-problems/3310_remove_methods_from_project.py) | Needs Review | 2026-08-09 | 1 |
| 2026-08-06 | 3345 | ✔️ | 🟢 Easy | Enumeration / Digit Processing | [Smallest Divisible Digit Product I](https://leetcode.com/problems/smallest-divisible-digit-product-i/) | [3345_smallest_divisible_digit_product_i.py](daily-problems/3345_smallest_divisible_digit_product_i.py) | Needs Review | 2026-08-09 | 0 |

## Programming Skills Study Plan

### Basic Implementation

| Completed | Difficulty | Pattern | Problem | Solution | Completed On |
| :---: | --- | --- | --- | --- | --- |
| ✔️ | 🟢 Easy | Two Pointers / String Building | [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | [1768_merge_strings_alternately.py](study-plan-problems/1768_merge_strings_alternately.py) | 2026-07-17 |

## Tricks

| Trick | When To Use It | Example |
| --- | --- | --- |
| Maintain a running total | When a stack/list changes over time but the final answer is the sum of remaining values | [682. Baseball Game](https://leetcode.com/problems/baseball-game/) |
| Use an auxiliary minimum stack | When a stack needs to return the current minimum in O(1) | [155. Min Stack](https://leetcode.com/problems/min-stack/) |
| Encode values as differences from the current minimum | When you want one stack to recover both values and previous minimums | [155. Min Stack](https://leetcode.com/problems/min-stack/) |
| Use only the requested extremes | When the problem asks about the smallest and largest values, avoid doing work across every value or pair | [1979. Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |
| Use `math.gcd` | When a problem needs the greatest common divisor and the custom Euclidean algorithm is not required | [1979. Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |
| Check outside-to-inside edges | When removing a marked group from a graph, verify no unmarked node points into that group | [3310. Remove Methods From Project](https://leetcode.com/problems/remove-methods-from-project/) |
| Use `math.prod` | When a problem needs the product of generated values, such as digits from a number | [3345. Smallest Divisible Digit Product I](https://leetcode.com/problems/smallest-divisible-digit-product-i/) |
| Extract digits with modulo/division | When you want O(1) extra space digit processing without converting to a string | [3345. Smallest Divisible Digit Product I](https://leetcode.com/problems/smallest-divisible-digit-product-i/) |
| Save `next_node` before rewiring | When reversing a linked list, store the next node before changing `current.next` | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |
| Use a dummy node | When building or relinking a linked list and the first node would otherwise need special handling | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) |
| Use dummy head and tail nodes | When a linked list design problem needs clean front/end insertions and removals without special-casing empty or one-node lists | [707. Design Linked List](https://leetcode.com/problems/design-linked-list/) |
