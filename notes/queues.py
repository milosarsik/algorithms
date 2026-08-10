# Queues

# A queue stores values in FIFO order:
# first in, first out.
#
# The main operations are:
# - enqueue: add to the back/right of the queue
# - dequeue: remove from the front/left of the queue
#
# A linked-list queue can do both operations in O(1) time by keeping
# references to both ends of the queue.


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        # left points to the front of the queue.
        # right points to the back of the queue.
        self.left = None
        self.right = None

    def is_empty(self):
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        return self.left is None

    def enqueue(self, val):
        # Add a value to the back of the queue.
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        new_node = ListNode(val)

        if self.right:
            self.right.next = new_node
            self.right = new_node
        else:
            self.left = new_node
            self.right = new_node

    def dequeue(self):
        # Remove and return the value at the front of the queue.
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        if not self.left:
            return None

        value = self.left.val
        self.left = self.left.next

        # If the queue became empty, right must also be reset.
        if not self.left:
            self.right = None

        return value

    def print_values(self):
        # Print values from front to back.
        # Time Complexity: O(n)
        # Space Complexity: O(n), for the display list.
        values = []
        current = self.left

        while current:
            values.append(current.val)
            current = current.next

        print(values)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("After enqueues:")
queue.print_values()  # [10, 20, 30]

print("dequeue:", queue.dequeue())  # 10
queue.print_values()  # [20, 30]

print("dequeue:", queue.dequeue())  # 20
print("dequeue:", queue.dequeue())  # 30
print("dequeue empty:", queue.dequeue())  # None

queue.enqueue(40)
print("after enqueue into empty queue:")
queue.print_values()  # [40]


# Queue Complexity Summary
# Enqueue: O(1)
# Dequeue: O(1)
# Peek/front: O(1), if implemented by reading self.left.val
# Is empty: O(1)
# Print/traversal: O(n)
#
# Common mistake:
# When dequeue removes the last node, reset both self.left and self.right.
