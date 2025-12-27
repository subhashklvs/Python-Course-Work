Reservation_train_tickets_id=int(input("Enter booking train tickets id:"))
Reservation_train_tickets_name=input("Enter booking train tickets name:")
Reservation_train_tickets_from=input("Enter booking train tickets from:")
Reservation_train_tickets_to=input("Enter booking train tickets to:")
Reservation_train_tickets_date=input("Enter booking train tickets date:")
Reservation_train_tickets_seat_number=int(input("Enter booking train tickets seat number:"))
#list
Reservation_train_tickets_details=[Reservation_train_tickets_id,Reservation_train_tickets_name,Reservation_train_tickets_from,Reservation_train_tickets_to,Reservation_train_tickets_date,Reservation_train_tickets_seat_number]
#tuple
Reservation_train_tickets_details_tuple=(Reservation_train_tickets_id,Reservation_train_tickets_name,Reservation_train_tickets_from,Reservation_train_tickets_to,Reservation_train_tickets_date,Reservation_train_tickets_seat_number)
#set
Reservation_train_tickets_details_set={Reservation_train_tickets_id,Reservation_train_tickets_name,Reservation_train_tickets_from,Reservation_train_tickets_to,Reservation_train_tickets_date,Reservation_train_tickets_seat_number}
#dict
Reservation_train_tickets_details_dict={
    "Reservation_train_tickets_id":Reservation_train_tickets_id,
    "Reservation_train_tickets_name":Reservation_train_tickets_name,
    "Reservation_train_tickets_from":Reservation_train_tickets_from,
    "Reservation_train_tickets_to":Reservation_train_tickets_to,
    "Reservation_train_tickets_date":Reservation_train_tickets_date,
    "Reservation_train_tickets_seat_number":Reservation_train_tickets_seat_number
}
print("Train Ticket Reservation Details in List:",Reservation_train_tickets_details)
print("Train Ticket Reservation Details in Tuple:",Reservation_train_tickets_details_tuple)
print("Train Ticket Reservation Details in Set:",Reservation_train_tickets_details_set)
print("Train Ticket Reservation Details in Dictionary:",Reservation_train_tickets_details_dict)#Train Ticket Reservation Details Management System

# or # 

# 1. int – User ID
user_id = 102345

# 2. str – User name
user_name = "Sirimilla Swetha "

# 3. float – Wallet balance
wallet_balance = 1500.75

# 4. list – Transaction history
transaction_history = ["Recharge ₹199", "Bill Payment ₹450"]

# 5. tuple – Bank account details (fixed data)
bank_details = ("SBI Bank", "XXXX1234")

# 6. set – Unique offers applied
offers_applied = {"Cashback10", "NewUserOffer"}

# 7. dict – PhonePe user profile
phonepe_profile = {
    "User ID": user_id,
    "Name": user_name,
    "Balance": wallet_balance,
    "Bank": bank_details
}

# Display user details
print("📱 PhonePe Application")
print("----------------------")
print("User ID:", phonepe_profile["User ID"])
print("User Name:", phonepe_profile["Name"])
print("Linked Bank:", phonepe_profile["Bank"])
print("Wallet Balance: ₹", phonepe_profile["Balance"])

print("\nTransaction History:")
for transaction in transaction_history:
    print("-", transaction)

print("\nOffers Applied:")
for offer in offers_applied:
    print("-", offer)
    
# or #

# Input section

# int
user_id = int(input("Enter User ID: "))

# str
user_name = input("Enter User Name: ")

# float
wallet_balance = float(input("Enter Wallet Balance: "))

# tuple (fixed bank details)
bank_name = input("Enter Bank Name: ")
account_last_digits = input("Enter Last 4 Digits of Account: ")
bank_details = (bank_name, account_last_digits)

# list (transactions)
transaction1 = input("Enter Transaction 1: ")
transaction2 = input("Enter Transaction 2: ")
transaction_history = [transaction1, transaction2]

# set (offers)
offer1 = input("Enter Offer 1: ")
offer2 = input("Enter Offer 2: ")
offers_applied = {offer1, offer2}

# dict (PhonePe profile)
phonepe_profile = {
    "User ID": user_id,
    "User Name": user_name,
    "Wallet Balance": wallet_balance,
    "Bank Details": bank_details,
    "Transactions": transaction_history,
    "Offers": offers_applied
}

# Output section

print("\n📱 PhonePe Application Details")
print("------------------------------")
print("User ID:", phonepe_profile["User ID"])
print("User Name:", phonepe_profile["User Name"])
print("Wallet Balance: ₹", phonepe_profile["Wallet Balance"])
print("Bank Details:", phonepe_profile["Bank Details"])

print("\nTransaction History:")
for transaction in phonepe_profile["Transactions"]:
    print("-", transaction)

print("\nOffers Applied:")
for offer in phonepe_profile["Offers"]:
    print("-", offer)
