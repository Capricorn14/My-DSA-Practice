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
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while(temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()

print(my_linked_list.pop())

print(my_linked_list.pop())

print(my_linked_list.pop())