# ***************
# File: hw2_2_SinghM.py
# Program Description: Program that prints the harmonic, geometric, and arithmetic mean of two real numbers givenm by the user
# Input: 2 real number values are inputted by the user using their KeyboardInterrupt
# Output: The harmonic, geometric, and arithmetic means of the 2 real numbers
# Manmeet Singh
# Date: 9/22/21
# ***************

def main():
    import math
    NUMBER_OF_VARIABLES = 2
    # Prompts user to input 2 real numbers that are not 0 and have the same sign
    print("Enter two numbers which are not 0 and have the same sign.")
    num_1 = float(input("Number 1: "))
    num_2 = float(input("Number 2: "))

    # Calculates the harmonic, geometric, and arithmetic means of the 2 user given numbers
    harmonic_1 = 1 / num_1
    harmonic_2 = 1 / num_2
    harmonic_mean = NUMBER_OF_VARIABLES / (harmonic_1 + harmonic_2)
    geometric_mean = math.sqrt(num_1 * num_2)
    arithmetic_mean = (num_1 + num_2) / NUMBER_OF_VARIABLES

    # Prints the calculated harmonic, geometric, and arithmetic means of the 2 user given numbers
    print(f"The Harmonic mean is {harmonic_mean}")
    print(f"The Geometric mean is {geometric_mean}")
    print(f"The Arithmetic mean is {arithmetic_mean}")
    return

main()
