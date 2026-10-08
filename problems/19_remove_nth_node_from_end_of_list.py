# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Attempt (2026-10-08): user reports solving it on their own, with Grokking's
# vertical sequence as guidance. Both the original and cleaned versions follow.
# Confidence: High.
# Assumptions: the list is nonempty and 1 <= n <= its length.

# Algorithm in English:
# 1. Put a dummy node before head, and start slow and fast at dummy.
# 2. Advance fast by n links to create a fixed gap.
# 3. Move both pointers until fast is at the last node (fast.next is None).
# 4. slow is now immediately before the target. Bypass slow.next.
# 5. Return dummy.next, which also handles removal of the original head.

# Pointer-gap reminder:
# - Advance n times, then use while fast.next: fast stops at the LAST NODE.
# - Alternatively, advance n + 1 times, then use while fast: fast stops at None.
# Both combinations put slow before the target. Do not mix the gap and guard.
# Example: [1, 2, 3, 4, 5], n=2. After advancing fast: slow=dummy, fast=2.
# Moving together until fast=5 leaves slow=3; bypass 4 to get [1, 2, 3, 5].


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


# Original solution. O(L) time, O(1) extra space, where L is the list length.
def remove_nth_last_node(head, n):
    dummy = ListNode(-1, head)
    slow, fast = dummy, dummy

    i = 0
    while i != n:
        fast = fast.next
        i += 1

    # Correct: fast is already at the tail when n equals the list length.
    # The target is the head; returning its successor removes it.
    if not fast.next:
        return dummy.next.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next


# Cleaned solution. Same O(L) time and O(1) extra space; fewer special cases.
# It does not first count the list length, so it is a single-pass approach.
def remove_nth_last_node_cleaned(head, n):
    dummy = ListNode(-1, head)
    slow, fast = dummy, dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    # If n == L, the loop never runs and slow stays at dummy. This same line
    # removes the head, including a one-node list, without a separate branch.
    slow.next = slow.next.next
    return dummy.next


# Example helpers only: build actual nodes from values, then collect values
# for printing. Their O(L) storage is not part of the removal algorithm.
def build_linked_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


# Build a fresh list each time because removal changes the links.
for remove in (remove_nth_last_node, remove_nth_last_node_cleaned):
    print(remove.__name__)
    print("middle:", to_list(remove(build_linked_list([1, 2, 3, 4, 5]), 2)))  # [1, 2, 3, 5]
    print("head:", to_list(remove(build_linked_list([1, 2, 3]), 3)))  # [2, 3]
    print("tail:", to_list(remove(build_linked_list([1, 2, 3]), 1)))  # [1, 2]
    print("only node:", to_list(remove(build_linked_list([1]), 1)))  # []
