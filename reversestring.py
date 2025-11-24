string=[]
reverse=[]
def reverse_string(s):
    n=len(s)
    for i in range(n):
        string.append(s[i])
    while string:
        reverse.append(string.pop())
    return reverse


s=input("Enter the string:")
reversed=reverse_string(s)
print("Reversed string is:",reversed)

    
qwert