# ***************
# File: hw3_2_SinghM.py
# Program Description: Program for purchasing concert tickets based on sitting area and amount of tickets needed
# Input: Users will input the desired seating space and the amount of tickets that they need through their keyboard, and will have the option to quit anytime
# Output: Desired seats and the price for all of the tickets
# Manmeet Singh
# Date: 9/29/21
# ***************

def main():
    # Constants are defined
    seat_type = 0
    ticket_amount = 0
    price = 0.00
    seat_print = ""
    
    # User is first prompted for seating type
    print(f"Welcome to the ticket master. \n\tFor Orchestra tickets, please indicate o or O. \n\tFor Tier 1 tickets, please indicate t1 or T1. \n\tFor Tier 2 tickets, please indicate t2 or T2. \n\tFor Balcony seats, please indicate b or B. \n\tIf you would like to cancel the transaction at any time, type q or Q.")
    seat_type = input("Indicate your selection: ")

    # Based on the indicated choice of seat type by the user, the program will set the price for the tickets

    # Branches through orchestra seat types
    if (seat_type == "o") or (seat_type == "O"):
        print(f"\tFor orchestra front seats, indicate of or OF. \n\tFor orchestra center seats, please indicate oc or OC. \n\tFor orchestra back seats, please indicate ob or OB. \n\tOtherwise q or Q to quit.")
        seat_type = input("Indicate your selection here: ")
        if (seat_type == "of") or (seat_type == "OF"):
            price = 95.00
            seat_print = "Orchestra Front"
        elif (seat_type == "oc") or (seat_type == "OC") :
            price = 150.50
            seat_print = "Orchestra Center"
        elif (seat_type == "ob") or (seat_type == "OB"):
            price = 80.00
            seat_print = "Orchestra Back"
        elif (seat_type == "q") or (seat_type == "Q"):
            print("Transaction cancelled")
            return
        else:
            print("Invalid input. Please try again.")
            return
            
    # Tiered Seats        
    elif (seat_type == "t1") or (seat_type == "T1"):
        price = 250.00
        seat_print = "Tier 1"
    elif (seat_type == "t2") or (seat_type == "T2"):
        price = 150.00
        seat_print = "Tier 2"

    # Branches through balcony seat types
    elif (seat_type == "b") or (seat_type == "B"):
        print(f"\tFor balcony front seats, indicate bf or BF. \n\tFor balcony back seats, please indicate bb or BB. \n\tOtherwise q or Q to quit.")
        seat_type = input("Indicate your selection: ")
        if (seat_type == "bf") or (seat_type == "BF"):
            price = 60.00
            seat_print = "Balcony Front"
        elif (seat_type == "bb") or (seat_type == "BB"):
            price = 45.50
            seat_print = "Balcony Back"
        elif (seat_type == "q") or (seat_type == "Q"):
            print("Transaction cancelled")
            return
        else:
            print("Invalid input. Please try again.")
            return
    elif (seat_type == "q") or (seat_type == "Q"):
        print("Transaction cancelled")
        return
    else:
        print("Invalid input. Please try again.")
        return

    print(f"Price per {seat_print} ticket is {price:.2f}")
        
    # Next, the user is asked for quantity of tickets to purchase
    ticket_amount = (input("How many tickets would you like to purchase? And as always, type q or Q to quit: "))
    if (ticket_amount == "q") or (ticket_amount == "Q"):
        print("Transaction cancelled")
        return
    price = price * int(ticket_amount)
    
    # Finally, the total price of the transaction will be given and the user will be asked to confirm their purchase
    print(f"The total price for {ticket_amount} {seat_print} tickets is ${price:.2f}.")
    confirm = input("Would you like to confirm the purchase? Indicate Y if so. If not, indicate N: ")
    if (confirm == "Y"):
        print("Please enter your name and your mailing address.")
        name = input("Name: ")
        mailing_address = input("Mailing Address: ")
        print("Congratulations on your purchase!")
    if (confirm == "N"):
        print("Goodbye")
        return

    return
    
main()
