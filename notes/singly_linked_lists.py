# Singly Linked Lists

# A singly linked list stores values in nodes.
# Each node has:
# - val: the stored value
# - next: a reference to the next node
#
# Unlike arrays, linked list nodes do not need to be contiguous in memory.
# To move through the list, you follow next pointers one node at a time.


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        # Dummy node makes edge cases easier.
        # The real first value starts at self.head.next.
        self.head = ListNode(-1)
        self.tail = self.head

    def insert_end(self, val):
        # Insert at the end using the tail pointer.
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        # Remove the node at the given index.
        # Time Complexity: O(n), because we traverse to the index.
        # Space Complexity: O(1)
        i = 0
        current = self.head

        # Stop with current pointing to the node before the one we remove.
        # The dummy head lets index 0 work the same as every other index.
        while i < index and current:
            i += 1
            current = current.next

        if current and current.next:
            if current.next == self.tail:
                self.tail = current

            current.next = current.next.next

    def print_values(self):
        # Print the list values.
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        current = self.head.next

        while current:
            print(current.val, "->", end=" ")
            current = current.next

        print()


def build_linked_list(values):
    # Build a linked list from a Python list.
    # Time Complexity: O(n)
    # Space Complexity: O(n), for the nodes created.
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head):
    # Traverse and print each value.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    current = head
    values = []

    while current:
        values.append(current.val)
        current = current.next

    print(values)


def append_to_tail(head, value):
    # Append to the end of the list.
    # Time Complexity: O(n), because we traverse to the tail.
    # Space Complexity: O(1)
    new_node = ListNode(value)

    if not head:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node
    return head


def delete_after(node):
    # Delete the node after the given node.
    # Time Complexity: O(1), if we already have the node reference.
    # Space Complexity: O(1)
    if node and node.next:
        node.next = node.next.next


def reverse_linked_list(head):
    # Reverse the list in place by rewiring next pointers.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


head = build_linked_list([1, 2, 3])
print("Original:")
print_linked_list(head)

head = append_to_tail(head, 4)
print("After append:")
print_linked_list(head)

delete_after(head)
print("After deleting node after head:")
print_linked_list(head)

head = reverse_linked_list(head)
print("After reverse:")
print_linked_list(head)

linked_list = LinkedList()
linked_list.insert_end(10)
linked_list.insert_end(20)
linked_list.insert_end(30)

print("LinkedList class:")
linked_list.print_values()

linked_list.remove(1)
print("After removing index 1:")
linked_list.print_values()


# Singly Linked List Complexity Summary
# Access by index: O(n)
# Search: O(n)
# Insert after known node: O(1)
# Delete after known node: O(1)
# Append with tail pointer: O(1)
# Append without tail pointer: O(n)
# Remove by index: O(n)
# In-place reversal: O(n) time, O(1) space
