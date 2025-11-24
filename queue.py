ticket=[]
n=100
front=-1
rear=-1

def enqueue(item):
    if front==-1 and rear==-1:
        front=0
        rear=0
        ticket.append(item)
    else:
        rear+=1
        ticket.append(item)

def dequeue():
    if front==-1 or front>rear:
        print("Queue is empty")
    else:
        item=ticket[front]
        front+=1
        return item

def display():
    if front==-1 or front>rear:
        print("Queue is empty")
    else:
        for i in range(front,rear+1):
            print(ticket[i])

if __name__=="__main__":
    while True:
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            item=input("Enter the item to enqueue: ")
            enqueue(item)
        elif choice==2:
            item=dequeue()
            if item:
                print("Dequeued item:",item)
        elif choice==3:
            display()
        elif choice==4:
            break
        else:
            print("Invalid choice")