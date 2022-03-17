# ***************
# File: hw4_2_SinghM.py
# Program Description: Program that displays given roles an dnumber of times the sum of the 2 dice rolls is 6 or 7
# Input: Number of times the dice is rolled, given by user through keyboard
# Output: The number of times the sum of the 2 rolls is 6 or 7 based on rolls
# Manmeet Singh
# Date: 10/20/21
# ***************

def main():
    import random
    success = 0
    SUCC_SUM_1 = 6
    SUCC_SUM_2 = 7
    
    # Queries user for number of rolls
    num_rolls = int(input("Enter desired number of rolls: "))

    # Determines rolls and sum of the 2 rolls, and sums of 6 or 7 are counted up
    for rolls in range(num_rolls):
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        print(f"{die_1}, {die_2}")
        if die_1 + die_2 == SUCC_SUM_1 or die_1 + die_2 == SUCC_SUM_2:
            success += 1

    # Prints number of times conditions are satisfied
    print(f"Number of successes (sum of dice is 6 or 7) is {success}")

    return

main()
