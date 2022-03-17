# ***************
# File: hw6_3_SinghM.py
# Program Description: Program that computes student grades
# Input: Grade Scale, Student name and ID's, individual grades, and average test score from user keyboard
# Output: Formatted name, grade scale, and ID along with final grades and average test score
# Manmeet Singh
# Date: 11/03/21
# ***************

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

def getData():

    scores = {}
    value = "x"

    value = (input("Enter Student ID and Test score, divided by a space: "))
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
        value = (input("Enter Student ID and Test score, divided by a space: "))

    return scores

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

def average(scores):
    sum_score = 0
    denom = len(scores.values())

    # Calculates the average of the scores
    for i in scores.values():
        sum_score += i

    avg_score = (sum_score / denom)

    return avg_score

def printScale(scale):
    alph = ["F", "D", "C", "B", "A"]
    for i in range(0, len(scale) + 1):
        if i == 0:
            print(f"{alph[i]}  {scale[i]} > score")
        elif i == 4:
            print(f"{alph[i]}       score > {scale[i - 1]} ")
        else:
            print(f"{alph[i]}  {scale[i - 1]} >= score > {scale[i]} ")



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



