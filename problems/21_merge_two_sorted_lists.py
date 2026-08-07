# 21. Merge Two Sorted Lists

# Attempt notes:
# - Completed in 26 minutes and 25 seconds.
# - The main cleanup was removing extra empty-list checks.
# - The merge loop and final remainder check were the right idea.
# - Cue for next time: use a dummy node when building or relinking a result list.

# Algorithm in English:
# 1. Create a dummy node before the real merged list.
# 2. Keep current pointing at the tail of the merged list.
# 3. While both lists still have nodes:
#    i. Compare the current node values.
#    ii. Link current.next to the smaller node.
#    iii. Move forward in the list that provided that node.
#    iv. Move current forward.
# 4. One list may still have nodes left over.
# 5. Link current.next to the remaining list.
# 6. Return dummy.next, because dummy is only a placeholder.


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


# My Attempt
# Time Complexity: O(m + n)
# Space Complexity: O(1)
def merge_two_lists_my_attempt(list1, list2):
    if not list1 and not list2:
        return None

    if not list1:
        return list2

    if not list2:
        return list1

    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


# Optimized / Cleaned Up
# Time Complexity: O(m + n)
# Space Complexity: O(1)
def merge_two_lists_iterative(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 if list1 else list2

    return dummy.next


# Time Complexity: O(m + n)
# Space Complexity: O(m + n), because recursion uses the call stack.
def merge_two_lists_recursive(list1, list2):
    if not list1:
        return list2

    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1

    list2.next = merge_two_lists_recursive(list1, list2.next)
    return list2


list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])
print("my attempt:", to_list(merge_two_lists_my_attempt(list1, list2)))  # [1, 1, 2, 3, 4, 4]

list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])
print("iterative:", to_list(merge_two_lists_iterative(list1, list2)))  # [1, 1, 2, 3, 4, 4]

list1 = build_linked_list([])
list2 = build_linked_list([0])
print("my attempt:", to_list(merge_two_lists_my_attempt(list1, list2)))  # [0]

list1 = build_linked_list([])
list2 = build_linked_list([0])
print("iterative:", to_list(merge_two_lists_iterative(list1, list2)))  # [0]

list1 = build_linked_list([])
list2 = build_linked_list([])
print("my attempt:", to_list(merge_two_lists_my_attempt(list1, list2)))  # []

list1 = build_linked_list([])
list2 = build_linked_list([])
print("iterative:", to_list(merge_two_lists_iterative(list1, list2)))  # []

list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])
print("recursive:", to_list(merge_two_lists_recursive(list1, list2)))  # [1, 1, 2, 3, 4, 4]
