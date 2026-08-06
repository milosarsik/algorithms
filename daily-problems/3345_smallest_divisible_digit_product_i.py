"""
3345. Smallest Divisible Digit Product I
"""

# Description:
# Given n and t, return the smallest integer greater than or equal to n whose
# digit product is divisible by t.
#
# Attempt notes:
# - Solved in 26 minutes, but this should feel faster for an Easy problem.
# - Main mistakes were Python/API recall, returning the wrong thing, and
#   comparing the wrong value.
# - Cue for next time: enumerate candidates, compute digit product, then check
#   product % t == 0.
#
# Algorithm in English:
# 1. Start checking numbers from n.
# 2. For each candidate number, compute the product of its digits.
# 3. If the digit product is divisible by t, return the candidate number.
# 4. A valid answer appears within at most 10 checks because any number with a
#    0 digit has digit product 0, and 0 is divisible by t.
#
# Why check only n through n + 9?
# In any 10 consecutive numbers, one number ends in 0.
# Example: from 23 to 32, the number 30 appears.
# Example: from 101 to 110, the number 110 appears.
# A number that contains digit 0 has digit product 0.
# Since 0 % t == 0 for any positive t, that number always works.
#
# Complexity note:
# The search checks at most 10 candidates. Each digit-product calculation takes
# O(d), where d is the number of digits in the candidate. With this problem's
# constraints, that is effectively constant time.

import math


# Time Complexity: O(10 * d), where d is the number of digits in n.
# Because n <= 100, this is effectively O(1).
# Space Complexity: O(d), because str(candidate) creates digit characters.
def smallest_number_math_prod(n, t):
    # This is still brute force / enumeration.
    # The only "Python trick" is converting the number to a string so we can
    # loop over its digits directly.
    for candidate in range(n, n + 10):
        # Example:
        # candidate = 123
        # str(candidate) -> "123"
        # int(digit) for digit in "123" -> 1, 2, 3
        # math.prod(...) -> 1 * 2 * 3 -> 6
        product = math.prod(int(digit) for digit in str(candidate))

        # product % t == 0 means product is divisible by t.
        # "not product % t" is the same check, but this is clearer.
        if product % t == 0:
            return candidate


# Time Complexity: O(10 * d), where d is the number of digits in n.
# Because n <= 100, this is effectively O(1).
# Space Complexity: O(1).
def smallest_number_manual_digits(n, t):
    for candidate in range(n, n + 10):
        product = 1

        # Use a copy so we can destroy num while keeping candidate available
        # to return at the end.
        num = candidate

        while num > 0:
            # num % 10 gives the last digit.
            # Example: 123 % 10 == 3
            product *= num % 10

            # num //= 10 removes the last digit.
            # Example: 123 // 10 == 12
            num //= 10

        if product % t == 0:
            return candidate


# Time Complexity: O(10 * d), where d is the number of digits in n.
# Because n <= 100, this is effectively O(1).
# Space Complexity: O(d), because str(candidate) creates digit characters.
def smallest_number_one_liner(n, t):
    # Same logic as smallest_number_math_prod, compressed with next(...).
    # Read it as:
    # "Return the first candidate in range(n, n + 10) whose digit product is
    # divisible by t."
    return next(
        candidate
        for candidate in range(n, n + 10)
        if math.prod(int(digit) for digit in str(candidate)) % t == 0
    )


# Time Complexity: O(10 * d), where d is the number of digits in n.
# Because n <= 100, this is effectively O(1).
# Space Complexity: O(1).
def smallest_number_with_helper(n, t):
    # This is probably the cleanest interview version:
    # - the main function says "search candidates"
    # - the helper says "compute digit product"
    def digit_product(num):
        product = 1

        while num > 0:
            product *= num % 10
            num //= 10

        return product

    return next(
        candidate
        for candidate in range(n, n + 10)
        if digit_product(candidate) % t == 0
    )


print(smallest_number_math_prod(10, 2))  # 10
print(smallest_number_manual_digits(10, 2))  # 10
print(smallest_number_one_liner(10, 2))  # 10
print(smallest_number_with_helper(10, 2))  # 10

print(smallest_number_math_prod(15, 3))  # 16
print(smallest_number_manual_digits(15, 3))  # 16
print(smallest_number_one_liner(15, 3))  # 16
print(smallest_number_with_helper(15, 3))  # 16

print(smallest_number_math_prod(23, 6))  # 23
print(smallest_number_manual_digits(23, 6))  # 23
print(smallest_number_one_liner(23, 6))  # 23
print(smallest_number_with_helper(23, 6))  # 23
