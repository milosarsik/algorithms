# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Algorithm in English:
# 1. Create an empty map from each previously seen value to its index.
# 2. Walk through nums and calculate the missing value: target - nums[i].
# 3. If that value is already in the map, return the two indices.
# 4. Otherwise, store the current value and index for later iterations.
# Check before inserting so the current element cannot pair with itself.

# Attempt notes:
# - Solved independently.
# - Renamed the map but missed a few references, causing inconsistent names.
# - After a rename, check every reference or use the editor's rename symbol.
# - Return indices, not values. Duplicate values can still use distinct indices.

# Brute force would check every pair: O(n^2) time and O(1) extra space.
# This approach uses average O(1) dictionary lookups to avoid the inner loop.
# Time Complexity: O(n) average, where n is the length of nums.
# Space Complexity: O(n) for the map of previously seen values.
def two_sum(nums, target):
    val_index_map = {}

    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in val_index_map:
            return [i, val_index_map[difference]]
        val_index_map[nums[i]] = i


print("two sum:", two_sum([2, 7, 11, 15], 9))  # [1, 0]
print("later pair:", two_sum([3, 2, 4], 6))  # [2, 1]
print("duplicate values:", two_sum([3, 3], 6))  # [1, 0]
print("negative values:", two_sum([-3, 4, 3, 90], 0))  # [2, 0]
