# Recursion
# Studied 2026-11-04: NeetCode one-branch/two-branch recursion and the recursion
# section of Grokking Algorithms by Aditya Bhargava.
#
# A recursive function calls itself on a smaller version of the problem.
# 1. Identify the base case: an answer that needs no further recursive calls.
# 2. Make progress toward that base case with every recursive call.
# 3. Return or combine the smaller answer as calls finish (unwind).
# Each active call has its own parameters/local variables on the call stack.
# These numeric examples assume nonnegative integer inputs.
# Complexity counts arithmetic as constant time and space as call-stack depth;
# Python's growing integers add costs beyond this introductory model.


# Two-branch recursion
# Base cases: F(0) = 0, F(1) = 1.
# Recursive case: F(n) = F(n - 1) + F(n - 2).
# Time: O(2^n) upper bound; branches repeatedly recompute the same subproblems.
# Space: O(n) stack depth, not O(2^n): both branches are not active in full
# at once. Python finishes the left recursive call before evaluating the right.
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# One-branch recursion
# Base case: 0! = 1.
# Recursive case: n! = n * (n - 1)!.
# Time: O(n). Space: O(n) for the call stack.
# factorial(3) waits for factorial(2), which waits for factorial(1), then 0.
# The returned answers unwind as 1 -> 1 -> 2 -> 6.
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


# Base case: n <= 1. Recursive case: countdown(n - 1).
# Time: O(n), space: O(n) stack depth for positive n.
# Print happens BEFORE the recursive call, so values appear in descending order.
# Using <= instead of == also stops a call starting at zero from recursing forever.
def countdown(n):
    print(n)

    if n <= 1:
        return n

    return countdown(n - 1)


# Ordinary nested calls, NOT recursion: none of these functions calls itself.
# greet pauses while greet2 runs, resumes, then pauses while bye runs.
# Each helper returns implicitly with None. Call-stack depth stays constant.
# For a fixed-length name: O(1) time and O(1) extra space.
# Including name length m, string concatenation/output takes O(m) time and space.
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
    print("how are you, " + name + "?")


def bye():
    print("ok bye!")


print("fibonacci(5):", fibonacci(5))  # 5
print("fibonacci(0):", fibonacci(0))  # 0
print("fibonacci(1):", fibonacci(1))  # 1
print("factorial(5):", factorial(5))  # 120
print("factorial(0):", factorial(0))  # 1
print("countdown(5):")
countdown(5)  # 5, 4, 3, 2, 1 on separate lines
print("countdown(0):")
countdown(0)  # 0, then stops
greet("maggie")


# Complexity Summary (constant-time arithmetic model)
# Factorial: O(n) time, O(n) stack space.
# Naive Fibonacci: O(2^n) time upper bound, O(n) stack space.
# Countdown: O(n) time, O(n) stack space for positive n.
# Nested greeting calls: O(1) stack depth; not recursive.
#
# Review cues:
# - State the base case and why each call moves closer to it.
# - Use return when the caller needs the computed result; printing is different.
# - Count total calls for time and maximum active call depth for stack space.
# - Fibonacci repeats work: memoization can cache answers, a later optimization.
# - Python has a recursion-depth limit and does not eliminate tail calls.
