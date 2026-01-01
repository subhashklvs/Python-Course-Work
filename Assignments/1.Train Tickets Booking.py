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

