parenthesis=[]
def is_balanced(expression):
    for i in expression:
        parenthesis.append(i)
    print("the expression is",parenthesis) 
    while expression:
        dictionary={')':'(','}':'{',']':'['}
        y=input("enter bracket to check")
        if y in dictionary:
            if len(parenthesis)==0:
                print("balanced")
                return
            elif parenthesis[-1]==dictionary[y]:
                parenthesis.pop()
                print("matched")
            else:
                print("not matched")
        else:
            print("invalid input")
            return
        
    
expression="({{[("
is_balanced(expression)
    



