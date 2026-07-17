# 155. Min Stack

# Algorithm in English:
# 1. A normal stack can push, pop, and read the top in O(1).
# 2. The hard part is getMin in O(1), because scanning the whole stack would be O(n).
# 3. Store extra minimum information as values are pushed.
#    i. Two-stack approach: keep a second stack where each index stores the minimum
#       value at that same depth.
#    ii. Encoded approach: keep one stack of differences from the current minimum.
# 4. When popping, update the minimum-tracking data at the same time as the stack.
# 5. top and getMin can now return answers in O(1).


class MinStackTwoStacks:
    # Two stacks
    # Time Complexity: O(1) for push, pop, top, and getMin
    # Space Complexity: O(n)
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        if not self.min_stack:
            self.min_stack.append(value)
            self.stack.append(value)
        else:
            self.min_stack.append(min(self.min_stack[-1], value))
            self.stack.append(value)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None


class MinStackCompactTwoStacks:
    # Compact two stacks
    # Time Complexity: O(1) for push, pop, top, and getMin
    # Space Complexity: O(n)
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        value = min(value, self.min_stack[-1] if self.min_stack else value)
        self.min_stack.append(value)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


class MinStackEncoded:
    # One stack with encoded differences
    # Time Complexity: O(1) for push, pop, top, and getMin
    # Space Complexity: O(n)
    #
    # How the encoding works:
    # 1. Store value - current_min instead of storing value directly.
    # 2. If the difference is positive or zero, the pushed value is not smaller
    #    than the current minimum.
    # 3. If the difference is negative, the pushed value became the new minimum.
    #    That negative number is a signal that the old minimum is hidden inside it.
    # 4. To restore the old minimum after popping a negative value:
    #       encoded = value - old_min
    #       current_min = value
    #       old_min = current_min - encoded
    # 5. top has to decode too:
    #    i. If encoded > 0, actual value is current_min + encoded.
    #    ii. If encoded <= 0, actual value is current_min.
    def __init__(self):
        self.minimum = float("inf")
        self.stack = []

    def push(self, value):
        if not self.stack:
            self.stack.append(0)
            self.minimum = value
        else:
            encoded = value - self.minimum
            self.stack.append(encoded)

            if value < self.minimum:
                self.minimum = value

    def pop(self):
        if not self.stack:
            return

        encoded = self.stack.pop()

        if encoded < 0:
            self.minimum = self.minimum - encoded

    def top(self):
        encoded = self.stack[-1]

        if encoded > 0:
            return self.minimum + encoded
        else:
            return self.minimum

    def getMin(self):
        return self.minimum


def run_min_stack(stack_class):
    min_stack = stack_class()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(stack_class.__name__, "getMin:", min_stack.getMin())
    min_stack.pop()
    print(stack_class.__name__, "top:", min_stack.top())
    print(stack_class.__name__, "getMin:", min_stack.getMin())


run_min_stack(MinStackTwoStacks)
run_min_stack(MinStackCompactTwoStacks)
run_min_stack(MinStackEncoded)
