# ***************
# File: hw4_1_SinghM.py
# Program Description: Program that that stores appearance of odd and even numbers from a given amount of rolls
# Input: Number of times the dice is rolled, given by user through keyboard
# Output: Counts and stores number of times an odd or even number is rolled from the dice roll
# Manmeet Singh
# Date: 10/20/21
# ***************

def main():
    import random
    count = [0,0]

    # Queries user for number of rolls
    num_rolls = int(input("Enter desired number of rolls: "))

    # Determines even or odd value from number of rolls and stores whether they are even or odd numbers
    for rolls in range(num_rolls):
        dice_roll = random.randint(1, 6)
        if dice_roll % 2 == 0:
            count[0] += 1
        else:
            count[1] += 1

    # Prints out number of even rolls and odd rolls
    print(f"Even rolls: {count[0]}, Odd rolls: {count[1]})")

    return
main()
