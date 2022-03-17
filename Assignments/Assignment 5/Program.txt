# File: hw_5_SinghM_functions1.py
# Practice functions definition and testing using driver main()
# Name: Manmeet Singh
# Date: 10/27/21

import math
import random

# Function Definitions ============================================

# -----------------------------------------------------------------
# Function to compute area of a circle
# Parameters: radius r
# Return: the area of the circle with radius r
def area_circle(r):
    area = math.pi*r**2
    return area

# -----------------------------------------------------------------
# Function radius_circle(area)
# Function to compute area of circle
# Parameters: area a
# Return: the radius of the circle with area a
def radius_circle(a):
    radius = math.sqrt(a/math.pi)
    return radius

# -----------------------------------------------------------------
# Function word_count(text)
# Function to calculate word count
# Parameters: Sentence
# Return: Word Count
def word_count(text):
    word_list = text.split()
    count = len(word_list)
    return count

# -----------------------------------------------------------------
# Function initialize_list0(n)
# Function to initialize list
# Parameter: List length
# Return: List with desired length
def initialize_list0(n):
    list = []

    # Adds desired number of elements
    while n != 0:
        list.append(0)
        n -= 1
    return list
         
# -----------------------------------------------------------------
# Function initialize_list(n, value)
# Function to initialize list based on user inputted values
# Parameter: List length and desired character
# Return: List with desired length and value
def initialize_list(n, value):
    list = []
    
    # Adds desired number of elements with user-defined values
    while n != 0:
        list.append(value)
        n -= 1
    return list
        
# -----------------------------------------------------------------
# Function sum_rolls(n)
# Function to calculate the sum of n amount of rolls
# Parameter: Amount of rolls
# Return: Sum of the rolls
def sum_rolls(n):
    sum_rolls = 0
    roll_values = []

    # Rolls the die and appends roll values to list
    for length in range(n):
        roll = random.randint(1, 6)
        print(roll)
        roll_values.append(roll)
    sum_rolls = sum(roll_values)
    return sum_rolls

# -----------------------------------------------------------------
# Function list_count(lst)
# Function to create a dictionary that counts instances of a character within a list
# Parameter: List of numbers    
# Return: Dictionary with counts associated with 0, +, and - numbers
def list_count(lst):
    values = {"0": 0,
              "+": 0,
              "-": 0
              }
    # Increments dictionary based on given values
    for i in lst:
        if i == 0:
            values["0"] += 1
        elif i > 0:
            values["+"] += 1
        elif i < 0:
            values["-"] += 1
    return values

# main() ----------------------------------------------------------
# Driver for testing the functions
def main():

    # 1. testing area_circle(r)
    print("*** Testing area_circle(r) ***")
    areas = []
    for r in range(6):
        print(f'radius = {r},   area = {area_circle(r)}')
        areas.append(area_circle(r))
    

    # 2. testing radius_circle(area)
    print('*** Testing radius_circle(area) ***')
    for a in areas:
        print(f"area = {a}, radius = {radius_circle(a)}") 

    # 3. testing word_count(text)
    print('\n*** Testing word_count(text)***')
    text = input("Enter text here: ")
    while text != "":
        print(f"{text} has {word_count(text)} words")
        text = input("Enter text here: ")
        
    # 4. testing initialize_list0(n)
    print('\n*** Testing initialize_list0(n)***')
    for n in range(1, 6):
        print(f"{initialize_list0(n)}")
       
    # 5. testing initialize_list(n,value)
    print('\n*** Testing initialize_list(n, value)***')
    for n in range(1, 6):
        print(f"{initialize_list(n, '*')}")
        
    # Test 2
    desired_items = ["*", "10", "12.0", "-1"]
    for i in desired_items:
        print(f"{initialize_list(10, i)}")

    # 6. testing sum_rolls(n)
    print('\n*** Testing sum_rolls(n)***')
    test_values = [-1, 0, 1, 5]
    for n in test_values:
        print(f"Rolls: {n}, Total is {sum_rolls(n)}")
    
    
    # 7. testing list_count(lst)
    print('\n*** Testing list_count(lst) ***')
    lst = []
    print(f"\n{lst}")
    print(f"{list_count(lst)}")
    
    lst = [0, 0, 0]
    print(f"\n{lst}")
    print(f"{list_count(lst)}")

    lst = [1, 2, 3]
    print(f"\n{lst}")
    print(f"{list_count(lst)}")

    lst = [-1, -2, -3]
    print(f"\n{lst}")
    print(f"{list_count(lst)}")

    lst = [0, 1, -2]
    print(f"\n{lst}")
    print(f"{list_count(lst)}")
    

    return
# end of main()
 
main()    # call to main()

