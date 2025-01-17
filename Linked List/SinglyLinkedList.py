class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, value):
        self.value = value # Stored data
        self.next = None # Initialize pointer to the next node as None

class SinglyLinkedList:
    """A class representing a singly linked list."""
    def __init__(self, value=None):
        """
        Handles both empty initialization and initialization with a starting node
        """
        if value is None:  # Initialize an empty linked list
            self.head = None
            self.tail = None
            self.length = 0
        else:  # Initialize with a starting node
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
    
    def append(self, value):
        """
        Adds a new node with the given value to the end of the list.
        Handles the edge case when the list is empty.
        """
        new_node = Node(value)  # Create a new node
        if self.head is None:  # Edge case: list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Update the current tail's next pointer
            self.tail = new_node  # Move the tail to the new node
        self.length+=1
    
    def __repr__(self):
        """Provides a string representation of the linked list."""
        nodes = []
        current = self.head
        while current: # Traverse the Linked List 
            nodes.append(str(current.value)) # Add the data to the list
            current = current.next
        return " -> ".join(nodes) if nodes else "Empty Linked List"
    
            

if __name__=="__main__":
    # Create a node 
    node = Node(20)
    print(node) # [20|None]
    
    # Create an empty linked list
    list1 = SinglyLinkedList()
    print(list1.head)  # Output: None
    print(list1.tail)  # Output: None

    # Create a linked list with an initial node
    list2 = SinglyLinkedList(10)
    print(list2.head.value)  # Output: 10
    print(list2.tail.value)  # Output: 10

    # Creating an empty linked list
    sll = SinglyLinkedList()
    sll.append(5)  # Appending to an empty list
    print(sll.head.value)  # Output: 5
    print(sll.tail.value)  # Output: 5

    sll.append(10)  # Appending another value
    print(sll.head.value)  # Output: 5
    print(sll.head.next.value)  # Output: 10
    print(sll.tail.value)  # Output: 10

    # View the Linked List
    print(sll)