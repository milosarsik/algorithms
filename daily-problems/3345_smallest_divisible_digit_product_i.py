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
# Complexity note:
# The search checks at most 10 candidates. Each digit-product calculation takes
# O(d), where d is the number of digits in the candidate. With this problem's
# constraints, that is effectively constant time.

import math


# Time Complexity: O(10 * d), where d is the number of digits in n.
# Because n <= 100, this is effectively O(1).
# Space Complexity: O(d), because str(candidate) creates digit characters.
def smallest_number_math_prod(n, t):
    for candidate in range(n, n + 10):
        product = math.prod(int(digit) for digit in str(candidate))

        if product % t == 0:
            return candidate


# Time Complexity: O(10 * d), where d is the number of digits in n.
# Because n <= 100, this is effectively O(1).
# Space Complexity: O(1).
def smallest_number_manual_digits(n, t):
    for candidate in range(n, n + 10):
        product = 1
        num = candidate

        while num > 0:
            product *= num % 10
            num //= 10

        if product % t == 0:
            return candidate


# Time Complexity: O(10 * d), where d is the number of digits in n.
# Because n <= 100, this is effectively O(1).
# Space Complexity: O(d), because str(candidate) creates digit characters.
def smallest_number_one_liner(n, t):
    return next(
        candidate
        for candidate in range(n, n + 10)
        if math.prod(int(digit) for digit in str(candidate)) % t == 0
    )


# Time Complexity: O(10 * d), where d is the number of digits in n.
# Because n <= 100, this is effectively O(1).
# Space Complexity: O(1).
def smallest_number_with_helper(n, t):
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
