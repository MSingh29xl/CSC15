# ***************
# File: hw7_SinghM.py
# Program Description (main): Function that creates an acronym, sorts a list of non-negative numbers, calculates the word count for words in a sentence
# Input: String of words from user's keyboard
# Output: Pairs of words and ther corresponding counts in a character order
# Manmeet Singh
# Date: 12/7/21
# ***************

# Function: acronym()
# Function that creates an acronym of the first letters of a sentence that are capitalized
# Return: String of all the first letter of the words given 
def acronym():
    text = input("Enter text here: ").strip().split()
    acronym = ""
    for i in text:
        if i[0].isupper() == True:
            acronym += i[0]
    return acronym


# Function: processList(lst)
# Function that takes non-negative values and sorts them in ascending order
# Parameter: lst - A list of numbers
# Return: A new list of all the non-negative values in ascending order
def processList(lst):
    sortedList = sorted(lst)
    newList = []
    for i in sortedList:
        if i >= 0:
            newList.append(i)     
    return newList


# Function: wordCount(tokens)
# Function that creates a dictionary of words as keys and their number of appearances as values
# Parameter: tokens - A list of words
# Return: Dictionary that sorts appeareances of the words from the list parameter
def wordCount(tokens):
    word_dict = {}
    for i in tokens:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1
    return word_dict


def main():
    print("Testing acronym()")
    print(acronym())
    
    print(f"\nTesting processList()")
    lists = [ [0, -1, 9, -3, 4], [-1, -2, -3, -4, -5], [9, 2, 4, 3, 8] ] 
    for i in lists:
        print(processList(i))
    
    print(f"\nTesting wordCount()")
    text = input("Enter text here: ").strip().split()
    dict_final = wordCount(text)
    print(sorted(dict_final.items()))

main()
