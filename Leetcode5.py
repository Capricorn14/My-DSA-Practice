#Remove duplicates from a given Linked list and return a unique valued linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))


    def remove_duplicates(self):
        values = set()
        if self.length == 0:
            return None
        current = self.head
        previous = self.head
        values.add(current.value)
        while current.next is not None:
            current = current.next
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else: 
                previous = current
                values.add(current.value)