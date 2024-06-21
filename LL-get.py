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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#append a new node in the linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True             #optional

#append a new node to the beginning of the Linked List
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
        

    
    
my_linked_list = LinkedList(0)

my_linked_list.append(1)

my_linked_list.append(2)

my_linked_list.append(3)

print(my_linked_list.get(2))