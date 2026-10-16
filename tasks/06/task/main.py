balance = 1000
count = 0


while True:
    pin = input("PIN: ") == "1234"
    if pin == False:
        print("Wrong PIN")
        count += 1
        if count == 3:
            print("Access denied")
            break
    else:
        print(f"Balance: {balance:.2f}")
        print("1. Deposit")
        print("2. Withdraw")
        print("0. Exit")
        choice = int(input("Enter choice: "))
        if choice == 0:
            print("Goodbye")
            break
        elif choice == 1:
            deposit_amnt = float(input("Deposit amount: "))
            if deposit_amnt > 0:
                balance += deposit_amnt
                print("Deposit successful")
            else:
                print("Deposit cannot be 0")
        elif choice == 2:
            withdraw_amnt = float(input("Withdrawal amount: "))
            if withdraw_amnt <= balance and withdraw_amnt > 0:
                balance -= withdraw_amnt
                print("Withdrawal successful")
            else:
                print("Withdrawal amount cannot be 0 or more than balance")