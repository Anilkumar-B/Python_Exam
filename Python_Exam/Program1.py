"""1. ATM Simulation
- Create a program to simulate an ATM where users can:
- Check balance
- Deposit money
- Withdraw money
- Exit
- Use functions for each operation and implement proper input validation (e.g., insufficient
balance for withdrawal)."""


def display_menu():

    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit_money(balance):
    amount = input("Enter the amount to deposit: ")
    if amount.isdigit() or (amount.replace('.', '', 1).isdigit() and amount.count('.') < 2):
        amount = float(amount)
        if amount > 0:
            balance += amount
            print(f"You have deposited ${amount:.2f}. Your new balance is ${balance:.2f}.")
        else:
            print("Invalid amount. Please enter a positive number.")
    else:
        print("Invalid input. Please enter a valid number.")
    return balance

def withdraw_money(balance):
    amount = input("Enter the amount to withdraw: ")
    if amount.isdigit() or (amount.replace('.', '', 1).isdigit() and amount.count('.') < 2):
        amount = float(amount)
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"You have withdrawn ${amount:.2f}. Your new balance is ${balance:.2f}.")
    else:
        print("Invalid input. Please enter a valid number.")
    return balance

def atm_simulation():
    balance = 0.0  # Initialize the balance
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit_money(balance)
        elif choice == "3":
            balance = withdraw_money(balance)
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

atm_simulation()

