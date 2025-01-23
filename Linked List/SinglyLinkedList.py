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

    def __repr__(self):
        """Provides a string representation of the linked list."""
        nodes = []
        current = self.head
        while current: # Traverse the Linked List 
            nodes.append(str(current.value)) # Add the data to the list
            current = current.next
        return " -> ".join(nodes) if nodes else "Empty Linked List"
    
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
    
    def prepend(self, value):
        """Inserts a new node with the given value at the beginning of the list."""
        new_node = Node(value)  # Create a new node
        if self.head is None:  # Edge case: list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Point the new node to the current head
            self.head = new_node  # Update the head to the new node
        self.length+=1
    
    def insert_at_position(self, value, position):
        """
        Inserts a new node with the given value at the specified position.
        Positions are 0-based, where 0 is the beginning of the list. To append to the end give position as -1
        """
        if position<0 and position!=-1:
            raise ValueError("Position must be a non-negative integer!")
        
        new_node = Node(value=value)
        
        # prepend
        if position==0:
            self.prepend(value)
            return
        # append
        if position==-1:
            self.append(value)
            return
        
        
        # at any other position
        current = self.head
        count = 0
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            # Traverse to the node just before the desired position
            while current and count < position - 1:
                current = current.next
                count += 1

            if not current:  # If position is out of bounds
                raise ValueError("Position out of bounds.")

            # Insert the new node at the specified position
            new_node.next = current.next
            current.next = new_node
            
            # if the user provides the last index insted of -1 
            if new_node.next is None:
                self.tail = new_node
        
        # Increase length 
        self.length+=1
        
        
    
if __name__=="__main__":
    # Create a node 
    node = Node(20)
    print(node) # [20|None]
    
    ###### Create an empty linked list #######
    list1 = SinglyLinkedList()
    print(list1.head)  # Output: None
    print(list1.tail)  # Output: None

    ###### Create a linked list with an initial node ######
    list2 = SinglyLinkedList(10)
    print(list2.head.value)  # Output: 10
    print(list2.tail.value)  # Output: 10

    ###### Creating an empty linked list and append node ######
    sll = SinglyLinkedList()
    sll.append(5)  # Appending to an empty list
    print(sll.head.value)  # Output: 5
    print(sll.tail.value)  # Output: 5

    sll.append(10)  # Appending another value
    print(sll.head.value)  # Output: 5
    print(sll.head.next.value)  # Output: 10
    print(sll.tail.value)  # Output: 10
    
    ###### Prepend node ######
    sll = SinglyLinkedList()
    print(sll)  # Output: Empty Linked List

    # Insert at the beginning
    sll.prepend(10)
    print(sll)  # Output: 10

    sll.prepend(20)
    print(sll)  # Output: 20 -> 10

    sll.prepend(30)
    print(sll)  # Output: 30 -> 20 -> 10
    
    sll.insert_at_position(23,0)
    print(sll)
    
    sll.insert_at_position(232,1)
    print(sll)
    
    sll.insert_at_position(223,3)
    print(sll)
    
    sll.insert_at_position(34,sll.length)
    print(sll)
    
    sll.insert_at_position(35,-1)
    print(sll)