undo=[]
def undo_op():
    while True:
        y=input("enter y to add and n to undo:")
        if y=='y':
            z=input("enter letters:")
            undo.append(z)
            print("current string is:",undo)
        elif y=='n':
            if len(undo)==0:
                print("no letters to undo")
            else:
                undo.pop()
                print("current string is:",undo)
        else:
            print("invalid input")
            return

undo_op()