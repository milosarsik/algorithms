def gcd_of_odd_even_sums_euclidean(n):
    # Mathematical Euclidean algorithm
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def gcd(x, y):
        return x if y == 0 else gcd(y, x % y)

    return gcd(n * n, n * (n + 1))


def gcd_of_odd_even_sums_math(n):
    # Direct math
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    return n


n = 4

print("euclidean:", gcd_of_odd_even_sums_euclidean(n))
print("math:", gcd_of_odd_even_sums_math(n))

n = 5

print("euclidean:", gcd_of_odd_even_sums_euclidean(n))
print("math:", gcd_of_odd_even_sums_math(n))
