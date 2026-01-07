# module - a file containing Python code that can define functions, classes, and variables
# used to organize related code into a single file and reuse it across multiple programs
# to use a module, we need to import it using the import statement
# example of a module :

data= {
    1234: {'balance':2000,'transactions':[]},
    2341: {'balance':90000,'transactions':[]},
    3421: {'balance':56000,'transactions':[]},
   }

def login(pin):
    if pin in data:
        print("Login Successful")
        return True
    else:
        print("Invalid pin. Try Again!!!")
        return False

def checkbalance(pin):
    print(f"Balance Amount: ${data[pin]['balance']}")

def deposit(pin):
    amount = int(input("Enter the amount: "))
    data[pin]['balance']+=amount
    data[pin]['transactions'].append(f'${amount} is deposited++++++')
    print("Deposit Successful")

    
def withdraw(pin):
    amount = int(input("Enter the amount: "))
    if amount <= data[pin]['balance']:
        data[pin]['balance']-=amount
        data[pin]['transactions'].append(f'${amount} is withdraw-----')
        print("Amount is Withdraw successful")
    else:
        print("Insufficinet Balance")

def viewTransactions(pin):
    if data[pin]['transactions']:
        print("Transaction Histroy: ")
        for i in data[pin]['transactions']:
            print(i)
        else:
            print("End of Transactions")
    else:
        print("No Transactions")
        
        
            
            
#
            
import ATM as a

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
