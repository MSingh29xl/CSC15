# ***************
# File: hw6_1_SinghM.py
# Program Description: Program that prints information on the significance of the golden ratio, and its value
# Input: N/A
# Output: Information and value of the Golden Ratio
# Manmeet Singh
# Date: 11/03/21
# ***************

import math

# Function: godenRatioInfor()
# Function that prints the significance of the golden ratio
# Output: Significance of Golden Ratio
def goldenRatioInfo():
    print("The Golden ratio, represented symbolically as Phi, is a special ratio between two numbers, and is tied to the fibonacci sequence of growth, in which the the current value and previous value are added to each other to find the next value, and the ratio between these numbers and the larger number starts to approach this golden ratio. This sequence has been observed throughout many applications of life, including in the appearance of plant petals, growth rate of rabbits, ancient and modern architecture (as many artists have argued for the aesthetic beauty of the ratio), and expressed within mathematical concepts such as the quadratic formula and Kepler triangle.  ")

# Function: goldenRatioFormula
# Function that prints the formula for the golden ratio
# Output: Golden Ratio formula
def goldenRatioFormula():
    print(f"\nFormula: (1 + math.sqrt(5))/2\n")
    return

# Function: goldenRatio()
# Function that computes the golden ratio
# Output: Returns approximate value of the Golden Ratio
def goldenRatio():
    return ((1 + math.sqrt(5))/2)

def main():
    goldenRatioInfo()
    goldenRatioFormula()
    print(f"Golden Ratio Value (Approximate): {goldenRatio()}")
    return

main()
