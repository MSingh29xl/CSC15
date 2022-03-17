# ***************
# File: hw1_3_SinghM.py
# Program Description: Program that calculates the area of a rectangle with inputted length and width
# Input: User inputs the length and width of rectangle that they want the area for
# Output: The area of the rectangle
# Manmeet Singh
# Date: 9/14/21
# ***************

def main():
    # Reads length and width inputted by user from their keyboard
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculates the area based on user input
    area = length * width

    # Prints out the calculated area
    print(f"The area of the rectangle is: {area} cm^2")
    return
main()
