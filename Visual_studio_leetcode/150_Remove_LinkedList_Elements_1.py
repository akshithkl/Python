# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next  # Skip this node
            else:
                prev = curr  # Move prev forward
            curr = curr.next  # Move curr forward

        return dummy.next

# Helper to create linked list from Python list
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper to convert linked list to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

    # Testcase
input_list = [1, 2, 6, 3, 4, 5, 6]
val_to_remove = 6

    # Convert to linked list
head = create_linked_list(input_list)

    # Process
solution = Solution()
updated_head = solution.removeElements(head, val_to_remove)

    # Print output
output_list = linked_list_to_list(updated_head)
print("Output:", output_list)  # Expected: [1, 2, 3, 4, 5]


#  Two pointer Tecnique
# Time complexity : O(n)
#  Space complexity : O(1)
