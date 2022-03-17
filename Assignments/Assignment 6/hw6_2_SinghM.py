# ***************
# File: hw6_2_SinghM.py
# Program Description: Program that 
# Input: Real numbers x and k from user keyboard
# Output: Calculated values following specified conditions
# Manmeet Singh
# Date: 11/03/21
# ***************

# Function: intPower(x, k)
# Function that evaluates a given product/quotient based on its value
# Parameters: k is the integer value and x is the original value hat will be operated on
# Output: Calculated product from x and k, based on integer value
def intPower(x, k):
    prod = 1

    # Evaluates product based on value of integer k
    if k > 0:
        for i in range(k) :
            prod *= x
            
    elif k == 0:
        prod = 1
        
    elif k < 0:
        for i in range(k-1, -1):
            prod *= x
        prod = 1/prod

    return prod

def main():
    
    # Tests function using pre-defined values
    x = 10
    print(f"k     10^k\n----- ----------")
    for i in range(-5, 6):
        print(str(i) , end="    ")
        print(intPower(x, i))
    
main()
    
