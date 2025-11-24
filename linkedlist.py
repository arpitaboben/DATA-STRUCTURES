class NODE:
    def __init__(self,data):
        self.data=data
        self.next=None
   
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        new_node=NODE(data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_at_position(self,position,data):
        new_node=NODE(data)
        if position==0:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        for i in range(position-1):
            if temp is None:
                print("Position out of bounds")
                return
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    
    def insert_at_end(self,data):
        new_node=NODE(data)
        if self.head is None:
            self.head=new_node
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
            return
        temp.next=new_node
        new_node.next=None
    
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
    
    def search(self,data):
        temp=self.head
        while temp:
            if temp.data==data:
                print("value", data, "Found in address",temp)
            temp=temp.next
        return False


    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("NONE")

L1=LinkedList()
L1.insert_at_beginning(10)
L1.insert_at_beginning(12)
L1.insert_at_beginning("i")
L1.insert_at_end(10)
L1.display()
L1.search(10)
