# Project: Basic ATM System
# Features: Check Balance, Deposit, Withdraw, Exit

balance = 10000  # Initial amount
pin = 1234       # Default PIN

print("Welcome to Python Bank ATM")
user_pin = int(input("Please enter your 4-digit PIN: "))

if user_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print(f"Your current balance is: Rs. {balance}")
            
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient Balance!")
            else:
                balance = balance - amount
                print(f"Please collect cash. Remaining Balance: {balance}")
                
        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            balance = balance + amount
            print(f"Deposit Successful! New Balance: {balance}")
            
        elif choice == 4:
            print("Thank you for using Python Bank. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
else:
    print("Wrong PIN entered. Access Denied.")