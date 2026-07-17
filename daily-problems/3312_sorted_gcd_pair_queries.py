from bisect import bisect_left
from itertools import accumulate
from math import gcd


def gcd_values_brute_force(nums, queries):
    # Brute force
    # Time Complexity: O(n^2 log m + n^2 log n), where m is the max value in nums
    # Space Complexity: O(n^2)
    gcd_pairs = []
    n = len(nums)

    left = 0

    while left < n - 1:
        right = left + 1

        while right < n:
            gcd_pairs.append(gcd(nums[left], nums[right]))
            right += 1

        left += 1

    gcd_pairs.sort()

    return [gcd_pairs[q] for q in queries]


def gcd_values_optimized(nums, queries):
    # Counting + inclusion-exclusion + prefix sum + binary search
    # Time Complexity: O(n + m log m + q log m), where m is the max value in nums
    # Space Complexity: O(m)
    #
    # Algorithm in English:
    # 1. Count how many times each number appears in nums.
    # 2. For each possible gcd g, count how many nums are divisible by g.
    # 3. If k numbers are divisible by g, they form k * (k - 1) // 2 pairs
    #    whose gcd is at least g.
    # 4. That count includes pairs whose gcd is actually a larger multiple of g,
    #    like 2g, 3g, 4g, etc. Work from large g down to small g and subtract
    #    those already-known larger gcd counts. This is inclusion-exclusion.
    # 5. After this, count_gcd_pair[g] tells us exactly how many pairs have gcd g.
    # 6. Build a prefix sum so prefix_count[g] tells us how many sorted gcd pairs
    #    are <= g.
    # 7. For each query index, binary search the first gcd value whose prefix
    #    count is greater than query. That gcd is the value at that sorted index.
    max_num = max(nums)
    freq = [0] * (max_num + 1)

    for num in nums:
        freq[num] += 1

    count_gcd_pair = [0] * (max_num + 1)

    for curr_gcd in range(max_num, 0, -1):
        multiples_count = 0

        for multiple in range(curr_gcd, max_num + 1, curr_gcd):
            multiples_count += freq[multiple]

        count_gcd_pair[curr_gcd] = multiples_count * (multiples_count - 1) // 2

        # Remove pairs whose gcd is a larger multiple of curr_gcd.
        for larger_gcd in range(curr_gcd * 2, max_num + 1, curr_gcd):
            count_gcd_pair[curr_gcd] -= count_gcd_pair[larger_gcd]

    prefix_count = list(accumulate(count_gcd_pair))

    return [bisect_left(prefix_count, query + 1) for query in queries]


nums = [2, 3, 4]
queries = [0, 2, 2]

print("brute force:", gcd_values_brute_force(nums, queries))
print("optimized:", gcd_values_optimized(nums, queries))

nums = [4, 4, 2, 1]
queries = [5, 3, 1, 0]

print("brute force:", gcd_values_brute_force(nums, queries))
print("optimized:", gcd_values_optimized(nums, queries))

nums = [2, 2]
queries = [0, 0]

print("brute force:", gcd_values_brute_force(nums, queries))
print("optimized:", gcd_values_optimized(nums, queries))
