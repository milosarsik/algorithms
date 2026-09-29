# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

# Attempt: solved independently with high confidence on 2026-09-29.
# The first version used more explicit code rather than shorthand.
# That is not a correctness mistake; clarity matters more than brevity.

# Algorithm in English:
# 1. Place pointers at the first and last characters.
# 2. Move each pointer past non-alphanumeric characters (spaces/punctuation).
#    Keep checking left < right before accessing a character while skipping.
# 3. Compare the remaining characters in lowercase. A mismatch returns False.
# 4. Move both pointers inward and repeat until they meet or cross.
# 5. Return True when no mismatching pair exists.

# Review cues:
# - isalnum() accepts letters AND digits; isalpha() would skip digits.
# - lower() makes the comparison case-insensitive.
# - Short-circuit evaluation checks left < right before indexing the string.
# - An empty string or a string containing only punctuation returns True.
# - Compare in place rather than allocating a filtered copy of the string.

# Time Complexity: O(n), where n is the number of characters.
# Each pointer moves only inward, so the nested skip loops are linear overall.
# Space Complexity: O(1) extra space; only indices and single characters are used.
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


print("mixed case and punctuation:", is_palindrome("A man, a plan, a canal: Panama"))  # True
print("mismatch:", is_palindrome("race a car"))  # False
print("only punctuation:", is_palindrome(" .,! "))  # True
print("empty string:", is_palindrome(""))  # True
print("single character:", is_palindrome("a"))  # True
print("digits count too:", is_palindrome("0P"))  # False
