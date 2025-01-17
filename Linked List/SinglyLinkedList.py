class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, value):
        self.value = value # Stored data
        self.next = None # Initialize pointer to the next node as None
    
    def __repr__(self):
        return f"[{self.value}|{self.next}]"

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

