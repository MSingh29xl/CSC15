# ***************
# File: hw7_1_SinghM.py
# Program Description: 
# Input: Given scale, ID's and score of students  from user keyboard
# Output: 
# Manmeet Singh
# Date: 11/17/2021
# ***************

# Function to convert a list to list of ints. If successfull it changes the list
# Parameters: list lst
# Return: True if list converted successfully and False otherwise
# Note: if a list item cannot be converted to integer (ValueError), the
# function will not give run time error, it returns False. The caller can
# check the returned value and process it accordingly

def list2int(lst):
    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i])
        except ValueError:
            return False
    return True

# Predicate function to check if a list of numbers is strictly increasing
# Parameters: list lst, nonempty 
# Return: True if list strictly increasing and False otherwise

def isIncreasing(lst):
    
    return True    

# Predicate function to check if  list elements are withing specified interval
# Parameters: list lst,  and numbers l and h , l<=h 
# Return: True if all elements are between l and h, included and false otherwise

def isInInterval(lst, l, h):
    # fill in the code
    
    return True    

    

# Function to read a grade scale from keyboard
# Parameters: none
# Return: list scale, of length 4 of strictly increasing order, all values are
#          between 0 and 100


def getScale():

    scale = []
    print("Enter dividers for grade scale:\n"
          "    Four numbers between 0 and 100 in strictly increasing order.\n"
          "    When prompt, enter the numbers in order separated by space.\n")
    value = input("Enter the dividers here: ")
    scale = value.split

    if (len(scale) == 4) and (list2int(value) == True) and isIncreasing == True:
        return scale
    else:
        
    # *** FILL IN THE CODE
    # read the input and store in string scale

    # convert scale to list of integers, use list2int; keep track of the result returned

    # Notice that we want scale to be of length 4, converted to list of int successfully, be of length 4,
    # consisting of numbers between 0 and 100, and strictly increasing
    # For each of this conditions you should be able to check either using Python
    # built in functions, or the functions defined above

    # *** Fill in the code
    # while (scale not converted successfuly to list of int) or
    #       (list does not have 4 elements) or (the elements are not in range 0 to 100) or
    #       (the list is not strictly increasing):
    #     print invalid scale and ask that they enter the scale again.
    #
    # When done remove all comments that I have inserted in this stub
    
    return scale

# Predicate function to test if a number is in an interval [l, h]
# Parameters: number to test and interval limita l and  h
# Return: True if l<=number<=h and False otherwise

def inInterval(number, l, h):
    # write the code, make sure you do not return always True, take care of the below return
    return True


# Function to input strudent IDs and test scores 
# Parameters: none
# Return: dictionary grades{} with records id:score

def getData():
    print("Enter on one line, student ID and test score, separated by space.\n"
          "Continue this way with all students.\n"
          "When done just hit enter.\n"
          "Valid IDs are integers between 100 and 999 (included).\n"
          "Valid scores are between 0 and 100 (included).\n"
          "If you entered invalid ID or score per student you must re-enter"
          "correct values.\n")
          
    grades = {}
    entryline = input("Enter ID and score separated by space, or hit enter to quit: ")
                 
    while  entryline != '':
       # write  the code to process a line entered
       # if a valid record entered, store the record in the dictionary grades.
       # else print Invalid entry.
    
       entryline = input("Enter ID and score separated by space, or hit enter to quit: ")
        
    return grades
    

def main():
    scale = getScale()
    print(scale)
    grades = getData()
    return
main()
