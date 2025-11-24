history = []
forward = []

def page(visit):
    history.append(visit)

    print("You are on the page", visit)

def back():
    if len(history) <= 1:
        print("No pages in history")
    else:
        last_page = history.pop()     
        forward.append(last_page)      
        print("You are on the page", history[-1]) 

def history_display():
    if len(history) == 0:
        print("No pages in history")
    else:
        print("History of pages visited:")
        for i in history:
            print(i, end="->")

def forward_stack():
    if not forward:
        print("No forward pages available")
    else:
        page_to_visit = forward.pop()
        history.append(page_to_visit)
        print("You are on the page", page_to_visit)

def quit_browser():
    print("Exiting the browser")
    quit()

def main():
    while True:
        print("\n1. Go to page")
        print("2. Back")
        print("3. History")
        print("4. Forward")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            visit = input("Enter the page you want to visit: ")
            page(visit)
        elif choice == "2":
            back()
        elif choice == "3":
            history_display()
        elif choice == "4":
            forward_stack()
        elif choice == "5":
            quit_browser()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
