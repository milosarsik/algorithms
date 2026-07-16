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


def get_concatenation_iteration(nums):
    # Iteration I
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    length = len(nums)
    ans = [0] * (length * 2)

    for i in range(length):
        ans[i] = ans[i + length] = nums[i]

    return ans


def get_concatenation_enumerate(nums):
    # Iteration II
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    length = len(nums)
    ans = [0] * (length * 2)

    for i, num in enumerate(nums):
        ans[i] = ans[i + length] = num

    return ans


def get_concatenation(nums):
    # Shorthand
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    return nums + nums


nums = [1, 2, 1]

print("brute force:", get_concatenation_brute_force(nums))
print("iteration:", get_concatenation_iteration(nums))
print("enumerate:", get_concatenation_enumerate(nums))
print("shorthand:", get_concatenation(nums))

nums = [1, 3, 2, 1]

print("brute force:", get_concatenation_brute_force(nums))
print("iteration:", get_concatenation_iteration(nums))
print("enumerate:", get_concatenation_enumerate(nums))
print("shorthand:", get_concatenation(nums))
