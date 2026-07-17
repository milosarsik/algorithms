# 20. Valid Parentheses

# Algorithm in English:
# 1. Create a map from each closing bracket to its matching opening bracket.
# 2. Keep a stack of opening brackets seen so far.
# 3. Walk through the string one character at a time.
#    i. If the character is an opening bracket, push it onto the stack.
#    ii. If the character is a closing bracket, the stack must not be empty.
#    iii. Pop the most recent opening bracket and check that it matches.
# 4. At the end, the stack must be empty. If anything is left, some opening
#    brackets were never closed.


def is_valid_stack_map(s):
    # Stack with closing-to-opening map
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    bracket_key = {
        "}": "{",
        ")": "(",
        "]": "[",
    }

    stack = []

    for brace in s:
        if brace == "(" or brace == "{" or brace == "[":
            stack.append(brace)
        else:
            if not stack:
                return False

            if stack.pop() == bracket_key[brace]:
                continue
            else:
                return False

    return not stack


def is_valid_replace_pairs(s):
    # Repeatedly remove valid pairs
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")

    return s == ""


def is_valid_stack_peek(s):
    # Stack with peek before pop
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    stack = []
    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in s:
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False


s = "()"

print("stack map:", is_valid_stack_map(s))
print("replace pairs:", is_valid_replace_pairs(s))
print("stack peek:", is_valid_stack_peek(s))

s = "()[]{}"

print("stack map:", is_valid_stack_map(s))
print("replace pairs:", is_valid_replace_pairs(s))
print("stack peek:", is_valid_stack_peek(s))

s = "(]"

print("stack map:", is_valid_stack_map(s))
print("replace pairs:", is_valid_replace_pairs(s))
print("stack peek:", is_valid_stack_peek(s))
