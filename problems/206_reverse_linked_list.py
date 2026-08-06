# 206. Reverse Linked List

# Attempt notes:
# - Completed in about 15 minutes with AI help.
# - Missed the empty-list check at first.
# - The main sticking point was the pointer swap order.
# - Cue for next time: save next_node before changing current.next.

# Algorithm in English:
# 1. Keep two pointers:
#    i. previous points to the already-reversed part of the list.
#    ii. current points to the node we are rewiring now.
# 2. Before changing current.next, save current.next in next_node.
# 3. Point current.next backward to previous.
# 4. Move previous and current one step forward.
# 5. When current reaches None, previous is the new head.


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def to_list(head):
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    return values


# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_list_iterative(head):
    if not head:
        return None

    current = head
    previous = None

    while current:
        # Save the original next node before overwriting current.next.
        next_node = current.next

        # Reverse the pointer for the current node.
        current.next = previous

        # Move both pointers forward.
        previous = current
        current = next_node

    return previous


# Time Complexity: O(n)
# Space Complexity: O(n), because recursion uses the call stack.
def reverse_list_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


head = build_linked_list([1, 2, 3, 4, 5])
print("iterative:", to_list(reverse_list_iterative(head)))  # [5, 4, 3, 2, 1]

head = build_linked_list([1, 2])
print("iterative:", to_list(reverse_list_iterative(head)))  # [2, 1]

head = build_linked_list([])
print("iterative:", to_list(reverse_list_iterative(head)))  # []

head = build_linked_list([1, 2, 3, 4, 5])
print("recursive:", to_list(reverse_list_recursive(head)))  # [5, 4, 3, 2, 1]
