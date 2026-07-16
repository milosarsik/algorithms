# Stacks


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        # Add to the top of the stack
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        self.stack.append(n)

    def pop(self):
        # Remove from the top of the stack
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        return self.stack.pop()

    def peek(self):
        # Read the top of the stack without removing it
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        return self.stack[-1]


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("peek:", stack.peek())
print("pop:", stack.pop())
print("peek:", stack.peek())


# Stack Complexity Summary
# Push: O(1)
# Pop: O(1)
# Peek: O(1)
