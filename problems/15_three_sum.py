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

# Review 1 (2026-10-08): still Needs Review. Questions concerned the outer-loop
# bound, early exit, duplicate first values, pointer initialization, the missing
# pair-search loop, and the final pointer moves. Annotated review version below.

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
    # Sort to enable two-pointer movement and group duplicate values together.
    nums.sort()
    result = []
    n = len(nums)

    # Fix the first element, leaving at least two elements for the pair.
    for i in range(n - 2):
        # Skip duplicate first values to avoid repeating the same triplets.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # If the first value is positive, every remaining value is positive too.
        if nums[i] > 0:
            break

        # Search only after i so the three indices are distinct.
        left = i + 1
        right = n - 1
        # Find a pair whose sum is -nums[i].
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < 0:
                # Sum too small: try a larger value at the left pointer.
                left += 1
            elif current_sum > 0:
                # Sum too large: try a smaller value at the right pointer.
                right -= 1
            else:
                # Save the match before moving past duplicate values.
                result.append([nums[i], nums[left], nums[right]])
                # Skip repeated choices for the second element.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip repeated choices for the third element.
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # Move both pointers inward to search for a new pair.
                left += 1
                right -= 1

    return result


# User's review version, normalized to a standalone function.
# Time Complexity: O(n^2).
# Auxiliary Space: O(n) for Python sorting; output adds O(k) for k triplets.
def three_sum_review(nums):
    nums.sort()
    result = []
    n = len(nums)

    # My question: I had n - 1 instead of n - 2. What is the difference?
    # Answer: i must leave TWO positions after it, so its last useful index is
    # n - 3. range(n - 2) stops before n - 2. With n = 5, it visits 0, 1, 2.
    # range(n - 1) also visits i = 3, where left == right == 4. The guarded
    # while loop does nothing, so that extra iteration is redundant, not wrong.
    for i in range(n - 2):
        # My question: Why did >= fail a case?
        # Answer: zero must remain eligible: [0, 0, 0] is a valid triplet.
        # Only a POSITIVE first value makes every remaining triplet positive.
        if nums[i] > 0:
            break

        # My note: missed case.
        # Answer: skip a first value already used so we do not repeat triplets.
        # For [-1, -1, 0, 1], fixing either -1 would produce [-1, 0, 1].
        # i > 0 prevents comparing the first value with nums[-1].
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # My note: I had these one layer in instead of here.
        # Answer: initialize once for EACH fixed i, before the pair-search loop.
        # Putting them inside that loop resets its progress every iteration;
        # putting them outside the for loop fails to restart the search for i.
        left = i + 1
        right = n - 1

        # My note: completely missed this while loop.
        # Answer: one fixed value may need many pair checks. Continue until the
        # pointers meet. Without the loop, only the first pair is checked.
        # For [-4, -1, 0, 1, 3], -4 + -1 + 3 is too small, but advancing left
        # twice finds [-4, 1, 3]. Each iteration must recalculate the sum.
        while left < right:
            # Use current_sum instead of sum to avoid hiding Python's sum().
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

                # My question: Why move inward after the duplicate while loops?
                # Answer: those loops stop ON the last copy of each matched
                # value. These final steps move PAST those values to a new pair.
                # With [-2, 0, 0, 2, 2], a match at left=1/right=4 is followed
                # by duplicate skips to left=2/right=3, still holding 0 and 2.
                # The final moves cross the pointers and finish the search.
                # With [-1, 0, 1], neither skip loop moves at all. Omitting
                # these final steps would append the same triplet forever.
                left += 1
                right -= 1

    return result


print("mixed values:", three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print("repeated zeros:", three_sum([0, 0, 0, 0]))  # [[0, 0, 0]]
print("repeated pair:", three_sum([-2, 0, 0, 2, 2]))  # [[-2, 0, 2]]
print("no solution:", three_sum([0, 1, 1]))  # []
print("positive values:", three_sum([1, 2, 3]))  # []
print("fewer than three:", three_sum([0, 0]))  # []

print("review - zeros allowed:", three_sum_review([0, 0, 0]))  # [[0, 0, 0]]
print("review - repeated first value:", three_sum_review([-1, -1, 0, 1]))  # [[-1, 0, 1]]
print("review - several pair checks:", three_sum_review([-4, -1, 0, 1, 3]))  # [[-4, 1, 3], [-1, 0, 1]]
print("review - duplicate runs:", three_sum_review([-2, 0, 0, 2, 2]))  # [[-2, 0, 2]]
print("review - no duplicate skips:", three_sum_review([-1, 0, 1]))  # [[-1, 0, 1]]
print("review - fewer than three:", three_sum_review([0, 0]))  # []
