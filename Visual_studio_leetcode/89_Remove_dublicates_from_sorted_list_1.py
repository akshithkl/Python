class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip duplicate
            else:
                current = current.next
        return head

# Helper function to create linked list from list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))


values = [1, 1, 2, 3, 3]  # You can change this input
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

solution = Solution()
updated_head = solution.deleteDuplicates(head)

print("List after removing duplicates:")
print_linked_list(updated_head)



# | Aspect               | Complexity | Explanation                                                  |
# | -------------------- | ---------- | ------------------------------------------------------------ |
# | **Time Complexity**  | `O(n)`     | You traverse the list once, visiting each node exactly once. |
# | **Space Complexity** | `O(1)`     | No extra space is used, modification is done in-place.       |


# | Category           | Explanation                                                                                                                                                   |
# | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | **Algorithm**      | **Iterative Linked List Traversal** — goes node-by-node from head to tail.                                                                                    |
# | **Approach**       | **Linear Scan using one pointer** — checks if current and next nodes have the same value.                                                                     |
# | **Technique**      | **Two-pointer technique**: although only one pointer (`current`) is explicitly used, the 
#                          comparison with `current.next` makes it a form of two-pointer logic.                                                                                        |

# | **Data Structure** | Singly Linked List                                                                                                                                            |
# | **Optimization**   | In-place update — no extra list or memory used for storage.                                                                                                   |
