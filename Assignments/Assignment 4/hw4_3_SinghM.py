# ***************
# File: hw4_3_SinghM.py
# Program Description: Program that displays a histogram of the sum value of a given amount of dice rolls
# Input: Number of times the dice is rolled, given by user through keyboard
# Output: Asterisks of the values acheived from the sum of the 2 rolls in a histogram format
# Manmeet Singh
# Date: 10/20/21
# ***************

def main():
    
    import random
    
    #Initialize list
    sum_dict = {}
    for sum in range(2,13):
        sum_dict[sum]=''
    
    # Queries user for number of rolls
    num_rolls = int(input("Enter desired number of rolls: "))

    # Computes rolls and stores rolls within dictionary
    for rolls in range(num_rolls):
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        total_value = die_1 + die_2
        sum_dict[total_value] += "*"

    # Formats and prints histogram
    for key in sum_dict.keys():
        print(f"{key}: {sum_dict[key]}")
        
    return

main()
