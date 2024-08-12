class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_front(self, value):
        print("Inserting", value)
        
        # Step 1: Create a new Node
        new_node = Node(value)
        
        # Step 2: Set next of new_node to the current head
        new_node.next = self.head
        
        # Step 3: Set new_node as the head
        self.head = new_node
        
    def get_head_value(self):
        if self.head is None:
            return -1
        else:
            return self.head.value

# Create an instance of LinkedList
list = LinkedList()
list.insert_front(3)
print("The value at the head is:", list.get_head_value())

list.insert_front(2)
print("The value at the head is:", list.get_head_value())