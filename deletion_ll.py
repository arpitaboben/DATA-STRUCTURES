class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self):
        n1=Node(10)
        n2=Node(20)
        n3=Node(30)
        n1.next=n2
        n2.next=n3
        self.head=n1
        
    def delete_at_beginning(self):
        if self.head==None:
            print("it is empty")
        else:
            current=self.head
            self.head=current.next
    
    def delete_at_the_end(self):
        if self.head==None:
            print("it is empty")
        else:
            current=self.head
            if current.next.next==None:
                current.next=None
           
    def display(self):
        if self.head==None:
            print("it is empty")
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next
            print()
                





l1=Linkedlist()
l1.append()
l1.display()
l1.delete_at_beginning()
print("after deletion from the beggining")
l1.display()
l1.delete_at_the_end()
print("after deletion from the end")
l1.display()





