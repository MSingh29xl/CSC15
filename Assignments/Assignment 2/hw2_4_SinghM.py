# ***************
# File: hw2_4_SinghM.py
# Program Description: Program that calculates depreciated net value of your prize money after a certain amount of years
# Input: Name, original prize money amount, interest rate, and the number of years for which the user will recieve the award, inputted through the user's keyboard
# Output: Formatted name and monetary prize after a certain number of years
# Manmeet Singh
# Date: 9/22/21
# ***************

def main():
    # Prompts user for name, money amount, interest rate, and number of years in waiting for the award
    name = input("Winner's name: ")
    prize_amount = float(input("Enter prize amount in $: "))
    interest_rate = float(input("Enter interest rate in %: ")) 
    num_years = int(input("Enter number of years: "))

    # Calculates the depreciated value of the winnings after a certain number of years
    interest_rate = interest_rate / 100
    net_winning = prize_amount / ((1 + interest_rate) ** num_years)

    # Prints a formatted statement of the name and net winnings after deperciation is accounted Formatted
    print(f"\nThe present value of the prize for {name.title()} after {num_years} years is ${net_winning:.2f}")
    return

main()
