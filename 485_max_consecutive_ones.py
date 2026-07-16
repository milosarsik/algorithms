def find_max_consecutive_ones(nums):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    max_ones, curr_ones = 0, 0

    for num in nums:
        if num == 1:
            curr_ones += 1
        else:
            max_ones = max(max_ones, curr_ones)
            curr_ones = 0

    return max(max_ones, curr_ones)


def find_max_consecutive_ones_simple(nums):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    res, count = 0, 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            count = 0

        if res < count:
            res = count

    return res


def find_max_consecutive_ones_shorthand(nums):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    res, count = 0, 0

    for num in nums:
        count = count + 1 if num else 0
        res = max(res, count)

    return res


def find_max_consecutive_ones_brute_force(nums):
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    n, res = len(nums), 0

    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if nums[j] == 0:
                break
            cnt += 1
        res = max(res, cnt)

    return res


nums = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]

print("standard:", find_max_consecutive_ones(nums))
print("simple:", find_max_consecutive_ones_simple(nums))
print("brute force:", find_max_consecutive_ones_brute_force(nums))
print("shorthand:", find_max_consecutive_ones_shorthand(nums))

nums = [1, 0, 1, 1, 0, 1]

print("standard:", find_max_consecutive_ones(nums))
print("simple:", find_max_consecutive_ones_simple(nums))
print("brute force:", find_max_consecutive_ones_brute_force(nums))
print("shorthand:", find_max_consecutive_ones_shorthand(nums))
