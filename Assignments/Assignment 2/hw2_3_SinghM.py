# ***************
# File: hw2_3_SinghM.py
# Program Description: Program that prints personal data of a user
# Input: Name and phone number of the user inputted through the keyboard
# Output: Name and phone number in a properly formatted fashion
# Manmeet Singh
# Date: 9/22/21
# ***************

def main():
    # Prompts user for personal data
    name = input("Enter your name: ")
    phone_num = int(input("Enter your 10-digit integer number: "))

    # Formats name and derives area code and line number form phone number
    area_code = phone_num // 10000000
    prefix = phone_num // 10000
    prefix = prefix % 1000
    line_number = phone_num % 10000

    # Prints out the formatted name and number
    print(f"{name.title()} ({area_code}){prefix}-{line_number}")
    return

main()
