# ***************
# File: hw1_4_SinghM.py
# Program Description: Program that calculates average rainfall per day from a 30 day period
# Input: Total amount of rainfall within the 30 day period
# Output: The average rainfall during the 30 day period
# Manmeet Singh
# Date: 9/14/21
# ***************

def main():
    # Defining the constant for the amount of days in the period
    NUMBER_DAYS = 30
    
    # Reads the total rainfall in the period inputted by the user from their keyboard
    total_rainfall = int(input("Enter the total rainfall in inches: "))

    # Calculates the average rainfall within the 30 day period
    average_rainfall = float(total_rainfall / NUMBER_DAYS)

    # Outputs the average rainfall within the 30 day period
    print(f"The averege rainfall for the 30 day period was {average_rainfall:.2f} inches.")
    return
main()
