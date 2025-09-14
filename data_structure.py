inventory=[]
def add_item(item):
    #if you want to add multiple items, you can call this function in a loop
    number_of_item=int(input("Enter number of items to add: "))
    if number_of_item <= 0:
        print("Number of items must be greater than zero.")
        return
    for _ in range(number_of_item):
        sku = input("Enter SKU: ")
        # Check if SKU already exists
        if any(item['sku'] == sku for item in inventory):
            print("SKU already exists. Please enter a unique SKU.")
            continue
        
         #for checking if sku is empty

        name = input("Enter item name: ")
        #for checking if name is empty
        if not name.strip():
            print("Item name cannot be empty.")
            continue
        #for checking if name is aplha
        if name.replace(" ", "").isalpha() == False:
            print("Item name must contain only alphabetic characters and spaces.")
            continue

        #for checking if quantity is not aplha
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Quantity must be a valid integer.")
            continue
        #for checking if quantity is aplha
        if not isinstance(quantity, int):
            print("Quantity must be an integer.")
            continue
        

         #for checking if price is not aplha 
        price = int(input("Enter price: "))
        #for checking if price is negative
        try:
            price = float(price)
        except ValueError:
            print("Price must be a valid number.")
            continue
        #for checking if price is aplha
        if not isinstance(price, (int, float)):
            print("Price must be a number.")
            continue
        
        item = {
            'sku': sku,
            'name': name,
            'quantity': quantity,
            'price': price
        }

        
        inventory.append(item)
        print(f"Item {name} added successfully.")
        #call zero stock detection function
        zero_stock_detection()

#zero stock detection
def zero_stock_detection():
    zero_stock_items = [item for item in inventory if item['quantity'] == 0]
    if zero_stock_items:
        print("Items with zero stock:")
        for item in zero_stock_items:
            print(item)
    else:
        print("No items with zero stock.")
    
   
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item in inventory:
        print(f"SKU: {item['sku']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']:.2f}")
    
#for searching an item by SKU
def search_item(sku):
    for item in inventory:
        if item['sku'] == sku:
            return item
    return None

#for searching an item by name
def search_item_by_name(name):
    for item in inventory:
        if item['name'].lower() == name.lower():
            return item
    return None

#inventory overflow check
def check_inventory_overflow():
    if len(inventory) > 5:
        print("Warning: Inventory overflow. More than 100 items in inventory.")
    else:
        print("Inventory is within limits.")

#for updating an item quantity
def update_item_quantity(sku, new_quantity):
    item = search_item(sku)
    if item:
        try:
            if new_quantity < 0:
                raise ValueError("New quantity cannot be negative.")
            item['quantity'] = new_quantity
            print(f"Updated quantity for SKU {sku} to {new_quantity}.")
        except ValueError as e:
            print(e)
    else:
        print("Item not found.")

#to calculate total and avg stock
def total_avg_stock(inventory):
    if not inventory:
        return 0, 0
    total_stock = sum(item['quantity'] for item in inventory)
    avg_stock = total_stock / len(inventory)
    #to round off avg stock to 2 decimal places
    avg_stock = round(avg_stock, 2)
    return total_stock, avg_stock


#to calculate item with max stock
def item_with_max_stock(inventory):
    if not inventory:
        return None
    max_item = max(item['quantity'] for item in inventory)
    return max_item

#main function to run the inventory management system
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Search Item by SKU")
        print("4. Search Item by Name")
        print("5. Update Item Quantity")
        print("6. Check Inventory Overflow")
        print("7. Calculate Total and Average Stock")
        print("8. Item with Maximum Stock")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item({})
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            sku = input("Enter SKU to search: ")
            item = search_item(sku)
            if item:
                print(f"Found item: {item}")
            else:
                print("Item not found.")
        elif choice == '4':
            name = input("Enter name to search: ")
            item = search_item_by_name(name)
            if item:
                print(f"Found item: {item}")
            else:
                print("Item not found.")

        elif choice == '5':
            sku = input("Enter SKU of the item to update: ")
            new_quantity = int(input("Enter new quantity: "))
            update_item_quantity(sku, new_quantity)

        elif choice == '6':
            check_inventory_overflow()

        elif choice == '7':
            total, avg = total_avg_stock(inventory)
            print("Total stock:", total)
            print("Average stock:", avg)

        elif choice == '8':
            max_item = item_with_max_stock(inventory)
            if max_item:
                print("Item with maximum stock:", max_item)
                print("Details of item(s) with maximum stock:")
                for item in inventory:
                    if item['quantity'] == max_item:
                        print(item)
                print("Inventory is empty.")

        elif choice == '9':
            print("Exiting program.GOOD BYE!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()




