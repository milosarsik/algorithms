def remove_element_brute_force(nums, val):
    # Brute force
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    tmp = []
    for num in nums:
        if num == val:
            continue
        else:
            tmp.append(num)

    for i in range(len(tmp)):
        nums[i] = tmp[i]

    return len(tmp)


def remove_element_two_pointers(nums, val):
    # Two pointers I
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    write = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[write] = nums[i]
            write += 1

    return write


def remove_element_swap_with_end(nums, val):
    # Two pointers II
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    left, right = 0, len(nums)

    while left < right:
        if nums[left] == val:
            right -= 1
            nums[left] = nums[right]
        else:
            left += 1

    return right

nums = [3, 2, 2, 3]
val = 3

brute_force_nums = nums.copy()
k = remove_element_brute_force(brute_force_nums, val)
print("brute force:", k, brute_force_nums[:k])

two_pointers_nums = nums.copy()
k = remove_element_two_pointers(two_pointers_nums, val)
print("two pointers:", k, two_pointers_nums[:k])

swap_with_end_nums = nums.copy()
k = remove_element_swap_with_end(swap_with_end_nums, val)
print("swap with end:", k, swap_with_end_nums[:k])

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

brute_force_nums = nums.copy()
k = remove_element_brute_force(brute_force_nums, val)
print("brute force:", k, brute_force_nums[:k])

two_pointers_nums = nums.copy()
k = remove_element_two_pointers(two_pointers_nums, val)
print("two pointers:", k, two_pointers_nums[:k])

swap_with_end_nums = nums.copy()
k = remove_element_swap_with_end(swap_with_end_nums, val)
print("swap with end:", k, swap_with_end_nums[:k])
