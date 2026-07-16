def get_concatenation_brute_force(nums):
    # Brute force
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    ans = []

    for num in nums:
        ans.append(num)

    for num in nums:
        ans.append(num)

    return ans


def get_concatenation(nums):
    # Shorthand
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    return nums + nums


nums = [1, 2, 1]

print("brute force:", get_concatenation_brute_force(nums))
print("shorthand:", get_concatenation(nums))

nums = [1, 3, 2, 1]

print("brute force:", get_concatenation_brute_force(nums))
print("shorthand:", get_concatenation(nums))
