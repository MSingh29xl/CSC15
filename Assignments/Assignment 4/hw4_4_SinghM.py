# ***************
# File: hw4_4_SinghM.py
# Program Description: Program that 
# Input: No input is received from the user
# Output: The values of the rolled faces and the number of rolls that are not larger than the face value of the previous roll
# Manmeet Singh
# Date: 10/20/21
# ***************

def main():
    import random

    #Initialize list and variables
    rolled_faces = []
    previous_roll = 0
    successful_rolls = 0
    successful_rolls_value = 0
    curr_roll = 1

    #Performs rolls while keeping face values and comparing previous roll to current roll
    while curr_roll >= previous_roll:
        curr_roll = random.randint(1, 6)
        rolled_faces.append(curr_roll)
        
        if curr_roll >= previous_roll:
            previous_roll = curr_roll
            successful_rolls_value += previous_roll
            successful_rolls += 1
        
    #Prints and formats the rolled faces, total value of all the rolls, and the amount of succesful rolls     
    print(f"All rolled faces: {rolled_faces}\nTotal of the successful rolls: {successful_rolls_value}\nNumber successful rolls: {successful_rolls}")

    return

main()
