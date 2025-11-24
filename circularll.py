class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def create(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n1
        self.head = n1

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        
        ptr.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next

        ptr.next = new_node
        new_node.next = self.head
    
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_begin(data)
            return

        ptr = self.head
        count = 0
        while count < position - 1 and ptr.next != self.head:
            ptr = ptr.next
            count += 1

        new_node.next = ptr.next
        ptr.next = new_node


    def display(self):
        if self.head is None:
            print("List is empty")
            return

        ptr = self.head
        while True:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
            if ptr == self.head:
                break
        print()
        


ll = Linkedlist()
ll.create()
print("Original circular linked list:")
ll.display()

ll.insert_at_begin(90)
print("After inserting 90 at the beginning:")
ll.display()

ll.insert_at_end(100)
print("After inserting 100 at the end:")
ll.display()

print("After inserting 25 at position 2:")
ll.insert_at_position(25, 2)
ll.display()




