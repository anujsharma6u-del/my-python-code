
correct_pin = 1234
balance = 5000
attempts = 3


while attempts > 0:
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("PIN accepted")
        break
    
    else:
       attempts -= 1
       print("Wrong PIN")

       if attempts == 0:
           print("Remove the card and try again")

while True:
    print("\n--- ATM Menu---")
    print("1, Balance Check")
    print("2, Cash Withdrawal")
    print("3, Deposit")
    print("4, Exit")
    choice = int(input("Enter your choice(1-4): "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw."))
        if amount <= balance:
            balance -= amount
            print(f"{amount} withdrawn successfully")
            receipt = input("Do you want receipt? (yes/no): ")
            if receipt == "yes":
                print(f"Remaining balance: {balance}")
            else:
                print("No receipt")
        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid amount")

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
        