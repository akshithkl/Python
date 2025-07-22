# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1
            first, second = temp1, temp2

# Convert list to linked list
def list_to_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Convert linked list to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# MAIN ENTRY POINT

head = [1, 2, 3, 4]
linked_head = list_to_linked_list(head)

    # Debug print before reorder
print("Before reorder:", linked_list_to_list(linked_head))

sol = Solution()
sol.reorderList(linked_head)

# Output after reorder
print("After reorder:", linked_list_to_list(linked_head))



# | **Aspect**           | **Value**                                                           |
# | -------------------- | ------------------------------------------------------------------- |
# | **Algorithm**        | Linked List Manipulation                                            |
# | **Approach**         | Two Pointers + Reverse Second Half + Merge Alternately              |
# | **Technique**        | Fast and Slow Pointer, In-place Reversal, Pointer Rewiring          |
# | **Time Complexity**  | O(n) — Traverse list to find middle, reverse second half, and merge |
# | **Space Complexity** | O(1) — In-place manipulation, no extra memory used                  |
# | **Best Case**        | O(n) — Always needs full traversal regardless of list layout        |
# | **Worst Case**       | O(n) — Worst case is same as best (linear in all steps)             |
# | **Stable?**          | Not stable (reorders node positions)                                |
# | **In-Place?**        | Yes                                                                 |
# | **Input**            | Head of singly linked list                                          |
# | **Output**           | Modified list with reordered nodes in-place                         |
# | **Example Input**    | 1 → 2 → 3 → 4 → 5                                                   |
# | **Example Output**   | 1 → 5 → 2 → 4 → 3                                                   |
# | **Used For**         | Reordering nodes for problems like LeetCode 143 — Reorder List      |
