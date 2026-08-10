# 707. Design Linked List

# Attempt notes:
# - Did not fully solve independently.
# - Had to look up whether the ListNode class needed to be created.
# - Had to double-check index bounds for get, addAtIndex, and deleteAtIndex.
# - Hit a Time Limit Exceeded issue from creating a new ListNode inside ListNode.__init__.
# - Hit NoneType errors from walking past the node that needed to be updated.
#
# Mistakes to watch for:
# - ListNode.next should start as None, not ListNode(-1).
# - Use self.size inside class methods, not size.
# - get/delete valid indices are 0 through self.size - 1.
# - addAtIndex valid positions are 0 through self.size.
# - Return only when the index is invalid, not when it is valid.
# - For insert/delete, start at the dummy head and stop at the node before the target.
# - get should return curr.val, not the node itself.
# - deleteAtIndex must decrement self.size.

# Algorithm in English:
# 1. Create a dummy head node so inserts/deletes at index 0 are not special cases.
# 2. Track self.size so bounds checks are O(1).
# 3. For get:
#    i. Reject index if it is outside 0 <= index < self.size.
#    ii. Walk from the first real node to the index.
#    iii. Return the node value.
# 4. For addAtIndex:
#    i. Reject index if it is outside 0 <= index <= self.size.
#    ii. Walk from dummy head to the node before the insertion position.
#    iii. Link new_node.next to prev.next, then prev.next to new_node.
# 5. For deleteAtIndex:
#    i. Reject index if it is outside 0 <= index < self.size.
#    ii. Walk from dummy head to the node before the target.
#    iii. Skip the target with prev.next = prev.next.next.


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.size = 0

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        current = self.head.next

        for _ in range(index):
            current = current.next

        return current.val

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def addAtHead(self, val):
        self.addAtIndex(0, val)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        previous = self.head

        for _ in range(index):
            previous = previous.next

        new_node = ListNode(val)
        new_node.next = previous.next
        previous.next = new_node
        self.size += 1

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        previous = self.head

        for _ in range(index):
            previous = previous.next

        previous.next = previous.next.next
        self.size -= 1

    def values(self):
        values = []
        current = self.head.next

        while current:
            values.append(current.val)
            current = current.next

        return values


linked_list = MyLinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(1, 2)
print("list:", linked_list.values())  # [1, 2, 3]
print("get index 1:", linked_list.get(1))  # 2

linked_list.deleteAtIndex(1)
print("after delete:", linked_list.values())  # [1, 3]
print("get index 1:", linked_list.get(1))  # 3

linked_list.addAtIndex(2, 4)
print("append with addAtIndex:", linked_list.values())  # [1, 3, 4]

linked_list.addAtIndex(5, 9)
print("invalid add ignored:", linked_list.values())  # [1, 3, 4]

linked_list.deleteAtIndex(3)
print("invalid delete ignored:", linked_list.values())  # [1, 3, 4]
