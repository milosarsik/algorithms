"""
1979. Find Greatest Common Divisor of Array
"""

# Algorithm in English:
# 1. Find the smallest and largest values in the array.
# 2. Compute the GCD of only those two values.
#    i. Use the Euclidean formula: gcd(a, b) == gcd(b, a % b).
#    ii. Stop when the second value becomes 0.
# 3. Return that GCD.
# 4. Python also has this built in as math.gcd(a, b).

import math


# Time Complexity: O(n + log m), where n is len(nums) and m is max(nums).
# Space Complexity: O(log m), because the recursive gcd uses call stack space.
def find_gcd_manual(nums):
    def gcd(x, y):
        return x if y == 0 else gcd(y, x % y)

    max_val = float("-inf")
    min_val = float("inf")

    for num in nums:
        max_val = max(max_val, num)
        min_val = min(min_val, num)

    return gcd(min_val, max_val)


# Time Complexity: O(n + log m), where n is len(nums) and m is max(nums).
# Space Complexity: O(1).
def find_gcd_builtin(nums):
    min_val = min(nums)
    max_val = max(nums)

    return math.gcd(min_val, max_val)


print(find_gcd_manual([2, 5, 6, 9, 10]))  # 2
print(find_gcd_builtin([2, 5, 6, 9, 10]))  # 2

print(find_gcd_manual([7, 5, 6, 8, 3]))  # 1
print(find_gcd_builtin([7, 5, 6, 8, 3]))  # 1

print(find_gcd_manual([3, 3]))  # 3
print(find_gcd_builtin([3, 3]))  # 3
