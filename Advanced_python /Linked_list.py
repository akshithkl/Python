class Node:
    """A Node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Stores the data of the node
        self.next = None  # Pointer to the next node

class LinkedList:
    """A simple singly linked list implementation."""
    def __init__(self):
        self.head = None  # The head (first node) of the linked list

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty, set head to the new node
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node  # Append the new node

    def display(self):
        """Print all nodes in the linked list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        """Delete the first node with the specified key."""
        current = self.head

        # If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next  # Move head to the next node
            current = None  # Free up memory
            return

        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print(f"Node with data {key} not found.")
            return

        # Unlink the node
        prev.next = current.next
        current = None  # Free up memory

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Original List:")
    ll.display()
    
    print("After deleting 20:")
    ll.delete(20)
    ll.display()

    print("After deleting 40 (not in list):")
    ll.delete(40)
    ll.display()
