import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode(-1)  # Dummy node
        root = head

        # Push the head of each list into the heap
        for idx, element in enumerate(lists):
            if element:
                heapq.heappush(heap, (element.val, idx, element))

        # Process the heap
        while heap:
            val, idx, node = heapq.heappop(heap)  # Get the smallest element

            # Add this node to the result list
            head.next = ListNode(val)
            head = head.next

            # If there's a next node in this list, add it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return root.next

# Helper function to create a linked list from a list
def create_linked_list(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head: Optional[ListNode]):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(" -> ".join(map(str, elements)))


list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])

    # Combine the lists into an array
lists = [list1, list2, list3]

    # Merge the lists
solution = Solution()
merged_list = solution.mergeKLists(lists)

    # Print the result
print_linked_list(merged_list)
