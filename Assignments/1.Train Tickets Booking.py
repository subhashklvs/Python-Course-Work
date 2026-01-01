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

