import atm as a

pin = int(input("Enter the pin: "))

if a.login(pin):                

    while True:
        print('\n\n\n')
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("0. Exit")

        ch = int(input("Enter the choice: "))
        if ch == 1:
            a.checkbalance(pin)
        elif ch == 2:
            a.deposit(pin)
        elif ch == 3:
            a.withdraw(pin)
        elif ch == 4:
            a.viewTransactions(pin)
        elif ch == 0:
            print("Thank you")
            break
        else:
            print("Invalid choice")

