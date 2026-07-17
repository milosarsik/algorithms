def gcd_sum(nums):
    # Simulation with Euclidean algorithm
    # Time Complexity: O(n log n + n log m), where m is the max value in nums
    # Space Complexity: O(n)
    def gcd(x, y):
        return x if y == 0 else gcd(y, x % y)

    prefix_gcd = []
    max_val = 0

    for num in nums:
        max_val = max(max_val, num)
        prefix_gcd.append(gcd(num, max_val))

    prefix_gcd.sort()

    res = 0
    start, end = 0, len(prefix_gcd) - 1

    while start < end:
        res += gcd(prefix_gcd[start], prefix_gcd[end])
        start += 1
        end -= 1

    return res


nums = [2, 6, 4]

print("simulation:", gcd_sum(nums))

nums = [3, 6, 2, 8]

print("simulation:", gcd_sum(nums))
