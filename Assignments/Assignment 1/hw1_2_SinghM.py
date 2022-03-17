# ***************
# File: hw1_2_SinghM.py
# Program Description: Program that queries basic information about a user and prints it out
# Input: User types their queried information on their keyboard
# Output: The users basic information in a formatted way
# Manmeet Singh
# Date: 9/14/21
# ***************

def main():
    #Queries desired information from the user
    name = input("Enter your Name:")
    major = input("Enter your Major:")
    class_standing = input("Enter your Class Standing:")
    programming_experience = input("Enter your Programming Experience:")
    completed_math = input("Enter your highest completed Mathematics Course:")

    #Prints out the basic information that was inputted by the user
    print(f"Name:{name}")
    print(f"Major:{major}")
    print(f"Class Standing:{class_standing}")
    print(f"Programming Experience:{programming_experience}")
    print(f"Completed Math:{completed_math}")
    return
main()
