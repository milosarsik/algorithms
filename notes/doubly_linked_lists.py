# Doubly Linked Lists

# A doubly linked list stores values in nodes.
# Each node has:
# - val: the stored value
# - next: a reference to the next node
# - prev: a reference to the previous node
#
# The extra prev pointer lets us move in both directions.
# It also lets us remove from the end in O(1) if we have a tail pointer.


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        # Dummy head and tail nodes make insert/remove edge cases easier.
        # Real values always live between self.head and self.tail.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        return self.head.next == self.tail

    def insert_front(self, val):
        # Insert directly after the dummy head.
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        new_node = ListNode(val)
        first_node = self.head.next

        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node
        self.head.next = new_node

    def insert_end(self, val):
        # Insert directly before the dummy tail.
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        new_node = ListNode(val)
        last_node = self.tail.prev

        new_node.next = self.tail
        new_node.prev = last_node
        last_node.next = new_node
        self.tail.prev = new_node

    def remove_front(self):
        # Remove the first real node.
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        if self.is_empty():
            return None

        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head

        return node.val

    def remove_end(self):
        # Remove the last real node.
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        if self.is_empty():
            return None

        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail

        return node.val

    def print_values(self):
        # Print values from front to back.
        # Time Complexity: O(n)
        # Space Complexity: O(n), for the display list.
        values = []
        current = self.head.next

        while current != self.tail:
            values.append(current.val)
            current = current.next

        print(values)


linked_list = LinkedList()
linked_list.insert_front(20)
linked_list.insert_front(10)
linked_list.insert_end(30)
linked_list.insert_end(40)

print("After inserts:")
linked_list.print_values()  # [10, 20, 30, 40]

print("remove front:", linked_list.remove_front())  # 10
linked_list.print_values()  # [20, 30, 40]

print("remove end:", linked_list.remove_end())  # 40
linked_list.print_values()  # [20, 30]


# Doubly Linked List Complexity Summary
# Access by index: O(n)
# Search: O(n)
# Insert at front with dummy head: O(1)
# Insert at end with dummy tail: O(1)
# Delete from front with dummy head: O(1)
# Delete from end with dummy tail: O(1)
# Insert/delete after a known node reference: O(1)
