class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Convert list to linked list
def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to remove the nth node from the end of the list
def remove_nth_from_end(head, n):
    root = ListNode(0)
    root.next = head
    first = root
    second = root

    # Move 'first' n+1 steps ahead
    for i in range(n + 1):
        first = first.next

    # Move 'first' and 'second' until 'first' reaches the end
    while first is not None:
        first = first.next
        second = second.next

    # Skip the desired node
    second.next = second.next.next

    return root.next

# Initial linked list and value of n
head = create_linked_list([1, 2, 3, 4, 5])
n = 2

# Remove the nth node from the end
new_head = remove_nth_from_end(head, n)

# Print the modified linked list
print_linked_list(new_head)
