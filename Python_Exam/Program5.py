"""5. Shopping Cart
- Create a program to simulate a shopping cart:
- Add items (item name and price).
- View cart items.
- Calculate the total price.
- Exit.
- Use functions and a loop to allow multiple actions."""

def shopping_cart():

    cart = []  

    while True:
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total Price")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            item_name = input("Enter item name: ")
            item_price = float(input(f"Enter price for {item_name}: "))
            cart += [(item_name, item_price)]  
            print(f"{item_name} added to cart.")
        
        elif choice == "2":
            if not cart:
                print("Your cart is empty.")
            else:
                print("\n--- Your Cart ---")
                for item in cart:
                    print(f"{item[0]} - ${item[1]:.2f}")
        
        elif choice == "3":
            total = 0
            for item in cart:
                total += item[1]  
            print(f"Total Price: ${round(total,2)}")
        
        elif choice == "4":
            print("Exiting the shopping cart!")
            break
        
        else:
            print("Invalid choice, please try again.")

shopping_cart()
