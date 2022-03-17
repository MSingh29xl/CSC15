# ***************
# File: hw6_3_SinghM.py
# Program Description: Program that computes student grades
# Input: Grade Scale, Student name and ID's, individual grades, and average test score from user keyboard
# Output: Formatted name, grade scale, and ID along with final grades and average test score
# Manmeet Singh
# Date: 11/03/21
# ***************

# Function: getScale()
# Function that stores a scale from values given through user keyboard input
# Output: List that contains domains for user-defined scale
def getScale():

    scale = []
    prev_val = -1

    for i in range(0, 4):

        value = int(input(f"Enter valid integer #{i} (0-100) of increasing order for scale: "))

        # Input Validation
        while value <= prev_val or value > 100 or value < 0:
            print("Invalid input, try again")
            value = int(input(f"Enter valid integer #{i} (0-100) of increasing order for scale: "))

        # Appends scale values to list
        prev_val = value
        scale.append(value)

    return scale

# Function: getData()
# Function that collects ID's and scores given through user keyboard input
# Output: Dictionary of corresponding ID's and scores
def getData():

    scores = {}
    value = "x"

    value = int(input("Enter Student ID and Test score, divided by a space: "))
    while value != "":
        temp_list = value.split()

        # Input Validation
        while int(temp_list[0]) < 100 or int(temp_list[0]) > 999 or int(temp_list[1]) < 0 or int(temp_list[1]) > 100:
            print("Invalid input. Please try again.")
            value = input("Enter Student ID and Test score, divided by a space: ")
            temp_list = value.split()

        # Stores ID and grade to dictionary
        id = int(temp_list[0])
        score = int(temp_list[1])
        scores[id] = score
        value = input("Enter Student ID and Test score, divided by a space: ")

    return scores

# Function: setGrade(scale, a_score)
# Function that uses user defined scale to give a letter grade for a certain score
# Parameters: scale is defined scale from getScale, a_score is a score for the scores dictionary
# Output: Leyter grade for a given score
def setGrade(scale, a_score):
    letter = ""

    # Sets grades based on scale given by user
    if a_score <= scale[0]:
        letter = "F"
    elif a_score > scale[0] and a_score <= scale[1]:
        letter = "D"
    elif a_score > scale[1] and a_score <= scale[2]:
        letter = "C"
    elif a_score > scale[2] and a_score <= scale[3]:
        letter = "B"
    elif a_score > scale[3]:
        letter = "A"

    return letter

# Function: average(scores)
# Function that computes the average score of the class
# Parameters: List of ID's and accompanying scores from getdata()
# Output: Average score for the class
def average(scores):
    sum_score = 0
    denom = len(scores.values())

    # Calculates the average of the scores
    for i in scores.values():
        sum_score += i

    avg_score = (sum_score / denom)

    return avg_score

# Function: printScale(scale)
# Function that prints out a formatted version of the scale
# Parameter: User-provided scale list from getScale()
# Output: Formatted version o fteh scale that provides range justification for each letter
def printScale(scale):
    alph = ["F", "D", "C", "B", "A"]

    # Prints formatted version of scale
    print("\n  Grade Scale")
    for i in range(0, len(scale) + 1):
        if i == 0:
            print(f"{alph[i]}  {scale[i]} > score")
        elif i == 4:
            print(f"{alph[i]}       score > {scale[i - 1]} ")
        else:
            print(f"{alph[i]}  {scale[i - 1]} >= score > {scale[i]} ")


# Function: printGrades(grades)
# Function that prints out letter grades with their accompanying ID's
# Parameters: grades is the list of ID's and letter grades from the main function
# Output: List of ID's and letter grades for each student 
def printGrades(grades):
    print(f"\n   Grades\n ID    Grade\n ---   -----")
    for i,j in grades.items():
        print(f" {i}    {j}")



def main():
    # Initializes necessary variables/dictionaries and queries user for scale, ID's, and scores
    scale = getScale()
    scores = getData()
    grades = {}
    scale
    scores

    # Sets grades based on the user-set scale
    for i,j in scores.items():
        letter = setGrade(scale, j)
        letter
        grades[i] = letter

    avg_score = average(scores)
    avg_score

    # Prints average score, scale, and Final grades
    print(f"\nThe average score was {avg_score:.2f}")
    printScale(scale)
    printGrades(grades)

main()



