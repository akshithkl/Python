# Define the Node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Main logic to detect cycle
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False

# Helper to create linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

# Driver Code
values = [3, 2, 0, -4]
pos = 1  # cycle starting at node with value 2
head = create_linked_list_with_cycle(values, pos)

sol = Solution()
print(sol.hasCycle(head))  # Output: True
