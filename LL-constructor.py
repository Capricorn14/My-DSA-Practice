class Node:
    #creates a new node
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
    #creates a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # def append(self, value):
    # #creates a new node and add node to the end
    
    # def prepend(self, value):
    # #create a new node and add node to the beginning
    
    # def insert(self, index, value):
    #create a new node and insert the node at a certain index

my_linked_list = LinkedList(4)

print(my_linked_list.tail.value)