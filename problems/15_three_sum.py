# 15. 3Sum
# Source: supplied Grokking Coding Interview Patterns lesson solution.
# https://leetcode.com/problems/3sum/

# Attempt (2026-10-07): worked through the Grokking lesson and attempted the
# solution, but got stuck moving left/right inward and consulted the solution.
# Status: reviewed, not independently solved. Needs Review.
# Pointer movement reminder:
# - Sum < 0: increase left to try a larger value.
# - Sum > 0: decrease right to try a smaller value.
# - Sum == 0: save the match, skip duplicate values, then move BOTH pointers.
#   Keeping the same pair would repeat the match. Keeping either value while
#   changing only the other to a distinct value cannot give another zero sum.
# - Keep left < right so the pair uses two distinct indices.

# Algorithm in English:
# 1. Sort nums so moving left rightward increases the sum, and moving right
#    leftward decreases it. This changes the original input list.
# 2. Fix nums[i] as the first value, leaving at least two values after it.
#    i. Skip repeated first values to avoid repeating the same triplets.
#    ii. Stop if nums[i] > 0: all remaining values are also positive.
# 3. Search for the other two values with left = i + 1 and right = n - 1.
#    These positions ensure all three indices are distinct.
# 4. If the sum is too small, move left forward; if too large, move right back.
# 5. On a zero sum, save the triplet, skip repeated values at both pointers,
#    and move both pointers inward to search for a new pair.
# 6. Return all unique triplets. The output contains values, not indices.

# Review cues:
# - Reduce a three-value problem to a two-value problem: pair target = -nums[i].
# - Skip duplicate choices, not all duplicate input values: [-1, -1, 2] is valid.
# - Keep left < right in the duplicate loops before checking neighboring values.
# - Do not break at nums[i] == 0: [0, 0, 0] is a valid triplet.
# - Brute force checks all triples in O(n^3) time; fixing one value and scanning
#   the remaining range with two pointers reduces this to O(n^2).

# Time Complexity: O(n^2). Sorting is O(n log n); each fixed value has an O(n)
# scan. Duplicate-skipping loops only move the pointers inward during that scan.
# Auxiliary Space Complexity: O(n) worst case for Python's sort workspace.
# The pointer scan itself uses O(1) extra space.
# Output Space: O(k) for k unique triplets; total space is O(n + k).
def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


print("mixed values:", three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print("repeated zeros:", three_sum([0, 0, 0, 0]))  # [[0, 0, 0]]
print("repeated pair:", three_sum([-2, 0, 0, 2, 2]))  # [[-2, 0, 2]]
print("no solution:", three_sum([0, 1, 1]))  # []
print("positive values:", three_sum([1, 2, 3]))  # []
print("fewer than three:", three_sum([0, 0]))  # []
